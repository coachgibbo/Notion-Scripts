import random

import client

colors = ["default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red"]


def addSelectOptions(db_id, prop_name, options):
    url = f"https://api.notion.com/v1/databases/{db_id}"
    existing = []
    options_list = []

    db = client.get(url).json()
    if prop_name in db["properties"]:
        options_list = db["properties"][prop_name]["select"]["options"]
        existing = [opt["name"] for opt in options_list]

    for opt in options.split(','):
        if opt not in existing:
            options_list.append({"name": opt.lstrip(" "), "color": random.choice(colors)})

    select = {"options": options_list}
    prop = {"select": select}
    props = {prop_name: prop}
    body = {"properties": props}

    print(client.patch(url, body).status_code)


if __name__ == '__main__':
    addSelectOptions(input("Enter the database ID: "),
                     input("Enter the property name: "),
                     input("Enter a comma-separated list of values: "))
