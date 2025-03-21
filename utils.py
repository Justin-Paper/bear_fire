import json


def get_account_configs():
    with open('accounts.json', 'r', encoding='utf-8') as file:
        return json.load(file)
