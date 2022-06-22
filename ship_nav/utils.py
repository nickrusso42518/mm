from glob import glob
from pathlib import Path

def _get_filenames(input_path):
    fqfns = sorted(glob(f"{input_path}/*.csv"))
    courses = [Path(fqfn).stem for fqfn in fqfns]
    assert len(courses) == len(fqfns)
    return (fqfns, courses)
