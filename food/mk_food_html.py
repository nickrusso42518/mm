#!/usr/bin/env python

import re
from jinja2 import Environment, FileSystemLoader

ANNWN_FOOD_TYPE = 1432

# Read data from file, then close file
with open("food.txt", "r") as handle:
    text = handle.read()

# Define regex pattern
pattern = (
    r"^>\s+check\s+eqlookup\s+(?P<uuid>[0-9a-f]+).*"
    r"Item\s+'(?P<item>[\S ]+)'.*\s+food\s+will\s+provide\s+"
    r"(?:(?P<hrs>[\d+])\s+hours?\s+)?"
    r"(?:(?P<mins>\d+)\s+minutes?\s+)?.*"
    r"providing\s+(?P<buff>[\S\n ]+)\.\s+This\s+food\s+has"
)

# Create empty food list and compile regex (only do these once)
foods = []
regex = re.compile(pattern, re.DOTALL)

# Iterate over list of text chunks separated by double newline
for chunk in text.split("\n\n"):


    # Perform the regex match and test for success
    match = regex.search(chunk)
    if match:

        # Reformat captured values after parsing
        data = match.groupdict()
        data["buff"] = data["buff"].replace("\n", "")
        data["hrs"] = 0 if data["hrs"] is None else int(data["hrs"])
        data["mins"] = 0 if data["mins"] is None else int(data["mins"])

        # Append food data to list of foods
        foods.append(data)

        # Write chunk to disk
        with open(f"raw/{data['uuid']}.txt", "w") as handle:
            handle.write(chunk)

    # Did not match; print the text chunk for troubleshooting
    else:
        print(f"PARSING FAILED:\n{chunk}\n")

# Iterate over successfully parsed items, sorted by item (food name)
foods.sort(key=lambda n: n["item"].lower())
for food in foods:

    # Format the item in a compact format, example below:
    # 92. snapper fillets - 00:08 of +4 agility
    item, hrs, mins, buff = food["item"], food["hrs"], food["mins"], food["buff"]
    food_text = f"{item} - {hrs:02}:{mins:02} of {buff}"
    food["food_text"] = food_text

    # Build a URL using query parameters for use at annwn.info, example below:
    # https://annwn.info/item/search/?search=name&keyword=red+apple&
    #   type=1432&lowlevel=&highlevel=&sort=itemlevel
    food_url = (
        "https://annwn.info/item/search/?"
        "search=name&lowlevel=&highlevel=&sort=itemlevel"
        f"&type={ANNWN_FOOD_TYPE}"
        f"&keyword={item.replace(' ', '+')}"
    )
    food["food_url"] = food_url

    # Print the text and URL for troubleshooting at the console
    # print(food_text)
    # print(food_url)

# Setup the jinja2 templating environment and render the template
j2_env = Environment(
    loader=FileSystemLoader("."), trim_blocks=True, autoescape=True
)
template = j2_env.get_template("page.j2.html")
html = template.render(data=foods)
with open("index.html", "w") as handle:
    handle.write(html)
