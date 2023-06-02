import requests

from env import keys

headers = {"Notion-Version": "2022-02-22", "Authorization": keys.NOTION_API_KEY}


def get(url):
    return requests.get(url, headers=headers)


def post(url, payload):
    return requests.post(url, json=payload, headers=headers)


def patch(url, payload):
    return requests.patch(url, json=payload, headers=headers)


def delete(url, payload):
    return requests.delete(url, headers=headers)
