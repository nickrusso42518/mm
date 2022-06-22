 #!/use/bin/env python

import csv
import pytest
from utils import _get_filenames

MAX_SHIP_MARKS = 100
MAX_ROW_LENGTH = 4
X_BOUND = {"LOW": 0, "HIGH": 2299}
Y_BOUND = {"LOW": 0, "HIGH": 1499}
R_BOUND = {"LOW": 1, "HIGH": 100}
L_BOUND = {"LOW": 5, "HIGH": 40}

@pytest.fixture(scope="module")
def data():
    fqfns, courses = _get_filenames("ship_courses")
    data = {}
    for fqfn, course in zip(fqfns, courses):
        with open(fqfn, "r", encoding="utf-8-sig") as handle:
            data[course] = [row for row in csv.reader(handle)]

    return data

def test_check_duplicates(data):
    for csv_data in data.values():
        coords = [(row[1], row[2]) for row in csv_data]
        assert len(coords) == len(set(coords))

def test_cell_values(data):
    for csv_data in data.values():

        # Check length of table (number of rows)
        assert len(csv_data) <= MAX_SHIP_MARKS

        for row in csv_data:

            # Check and parse row values
            assert len(row) == MAX_ROW_LENGTH
            r, x, y, l = int(row[0]), int(row[1]), int(row[2]), row[3]

            # Check numeric values
            assert R_BOUND["LOW"] <= r <= R_BOUND["HIGH"]
            assert X_BOUND["LOW"] <= x <= X_BOUND["HIGH"]
            assert Y_BOUND["LOW"] <= y <= Y_BOUND["HIGH"]

            # Check location string
            assert not " " in l
            assert l == l.upper()
            assert L_BOUND["LOW"] <= len(l) <= L_BOUND["HIGH"]
