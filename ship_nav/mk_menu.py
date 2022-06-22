#!/use/bin/env python

import datetime
from jinja2 import Environment, FileSystemLoader
from utils import _get_filenames

def main(input_path):

    courses = _get_filenames(input_path)[1]
    data = {
        "per_line": 8,
        "courses": _get_filenames(input_path)[1],
        "timestamp": datetime.datetime.utcnow(),
    }

    j2_env = Environment(
        loader=FileSystemLoader("."), trim_blocks=True, autoescape=True
    )
    template = j2_env.get_template("ship_nav/alias_template.j2")
    rendered = template.render(data=data)

    with open("zcsv_menu.xml", "w") as handle:
        print(rendered)
        handle.write(rendered)

if __name__ == "__main__":
    main("ship_nav/courses")
