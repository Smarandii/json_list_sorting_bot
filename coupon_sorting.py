import datetime
import re
import json


def update_item_numbers(input_string):
    items = re.findall(r'"(.*?)"', input_string)
    updated_items = {}

    for idx, item in enumerate(items, start=1):
        updated_items[item] = idx

    return updated_items


def save_as_json(input_string):
    updated_items = update_item_numbers(input_string)
    json_output = json.dumps(updated_items, indent=0, ensure_ascii=False)
    file_name = f"outputs/output_{datetime.datetime.now().timestamp()}.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_output)
    return file_name


def save_as_string(input_file):
    with open(input_file, "r", encoding="utf-8") as json_file:
        json_string = json_file.read()
    json_string = json_string.replace("{", "")
    json_string = json_string.replace("}", "")

    return json_string
