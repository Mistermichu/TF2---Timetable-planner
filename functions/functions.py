import json
import os
from tkinter import messagebox

# Check line / post / station name requirements


def check_name_requirements_and_create(folder_name, file_name, messages, output_message, data_to_be_saved):
    file_path = os.path.join(folder_name, file_name + ".json")
    if os.path.exists(file_path):
        messagebox.showerror(messages["error"], messages["file_exists"])
    elif len(file_name) == 0:
        messagebox.showerror(
            messages["error"], messages[output_message])
    else:
        with open(file_path, 'w') as file:
            json.dump(data_to_be_saved, file)


# Language settings
def get_language(language):
    file_name = language + ".json"
    with open(os.path.join('messages', file_name), 'r', encoding='utf-8') as file:
        messages = json.load(file)
    return messages


def load_messages():
    with open(os.path.join('messages', 'en.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_available_languages():
    languages = []
    for file_name in os.listdir('messages'):
        if os.path.isfile(os.path.join('messages', file_name)):
            name, ext = os.path.splitext(file_name)
            if ext == ".json":
                languages.append(name)

    return languages

# Timetable functions


def generate_timetable():
    time_table = []
    for minute in range(0, 60):
        for second in range(0, 56, 5):
            new_time = [minute, second, False]
            time_table.append(new_time)
    return time_table
