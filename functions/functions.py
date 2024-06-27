import json
import os
from tkinter import messagebox

# Check new file input


def check_new_file(folder_name, file_name, file_data, messages):
    file_path = os.path.join(folder_name, file_name + ".json")
    if os.path.exists(file_path):
        messagebox.showerror(messages["error"], messages["file_exists"])
        return
    elif len(file_name) == 0:
        messagebox.showerror(
            messages["error"], messages["missing_data"])
        return
    else:
        if file_data:
            for key_value in file_data.values():
                if not key_value:
                    messagebox.showerror(
                        messages["error"], messages["missing_data"])
                    return
        with open(file_path, 'w') as file:
            json.dump(file_data, file)
            return


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


# Post List

class PostList():
    def __init__(self):
        self.posts = self.load_post_list()

    def load_post_list(self):
        post_list = []
        with open("post.json", "r", encoding="utf-8") as file:
            file_handler = json.load(file)
        for line in file_handler:
            post_list.append(line)
        return post_list

    def add(self, new_post, type, messages):
        post_list = self.posts
        if not new_post:
            messagebox.showerror(messages["error"], messages["missing_data"])
            return
        temporary_new_post = new_post.lower()
        for post in post_list:
            if temporary_new_post == post["post_name"].lower():
                messagebox.showerror(
                    messages["error"], messages["post_already_created"])
                return
        new_post = {
            "post_name": str(new_post),
            "type": type
        }
        post_list.append(new_post)
        post_list.sort(key=lambda x: x["post_name"])
        with open("post.json", "w", encoding="utf-8") as file:
            json.dump(post_list, file)

    def get_names(self):
        post_list = self.posts
        names = []
        for post in post_list:
            post_name = post["post_name"]
            names.append(post_name)
        return names
