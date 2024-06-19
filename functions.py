import json
import os


def get_language(language):
    messages = None
    while not messages:
        if language == "pl":
            with open(os.path.join('messages', 'pl.json'), 'r', encoding='utf-8') as file:
                messages = json.load(file)
        elif language == "en":
            with open(os.path.join('messages', 'en.json'), 'r', encoding='utf-8') as file:
                messages = json.load(file)
        else:
            print("Unsupported language. Please choose 'pl' or 'en'.")

    return messages


def load_messages():
    with open(os.path.join('messages', 'en.json'), 'r', encoding='utf-8') as file:
        return json.load(file)
