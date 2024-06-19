import tkinter as tk
import sys
import os


def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))
    from functions import get_language, load_messages

    def update_labels():
        button_add_line_section.config(text=messages["add_line_section"])
        button_manage_line_section.config(text=messages["manage_line_section"])
        button_add_line.config(text=messages["add_line"])
        button_manage_line.config(text=messages["manage_line"])
        button_add_station.config(text=messages["add_station"])
        button_manage_station.config(text=messages["manage_station"])
        button_add_branch_post.config(text=messages["add_branch_post"])
        button_manage_branch_post.config(text=messages["manage_branch_post"])
        button_add_standoff_post.config(text=messages["add_standoff_post"])
        button_manage_standoff_post.config(
            text=messages["manage_standoff_post"])
        button_select_language.config(text=messages["select_language"])
        button_exit.config(text=messages["exit"])

    def choose_language(new_language):
        nonlocal messages
        messages = get_language(new_language)
        update_labels()
        language_window.destroy()

    def on_select_language():
        global language_window
        language_window = tk.Toplevel(root)
        language_window.title(messages["select_language"])
        language_window.geometry("250x250")
        language_window.resizable(False, False)

        button_pl = tk.Button(
            language_window, text="pl", command=lambda: choose_language("pl"))
        button_pl.pack(fill=tk.X)

        button_en = tk.Button(
            language_window, text="en", command=lambda: choose_language("en"))
        button_en.pack(fill=tk.X)

    messages = load_messages()

    root = tk.Tk()
    root.title(messages["title"])
    root.geometry("500x500")
    root.resizable(False, False)

    # Button container
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Add line section
    button_add_line_section = tk.Button(
        root, text=messages["add_line_section"], command=lambda: None)
    button_add_line_section.pack(fill=tk.X)

    # Manage line section
    button_manage_line_section = tk.Button(
        root, text=messages["manage_line_section"], command=lambda: None)
    button_manage_line_section.pack(fill=tk.X)

    # Add Line
    button_add_line = tk.Button(
        root, text=messages["add_line"], command=lambda: None)
    button_add_line.pack(fill=tk.X)

    # Manage Line
    button_manage_line = tk.Button(
        root, text=messages["manage_line"], command=lambda: None)
    button_manage_line.pack(fill=tk.X)

    # Add station
    button_add_station = tk.Button(
        root, text=messages["add_station"], command=lambda: None)
    button_add_station.pack(fill=tk.X)

    # Manage station
    button_manage_station = tk.Button(
        root, text=messages["manage_station"], command=lambda: None)
    button_manage_station.pack(fill=tk.X)

    # Add branch post
    button_add_branch_post = tk.Button(
        root, text=messages["add_branch_post"], command=lambda: None)
    button_add_branch_post.pack(fill=tk.X)

    # Manage branch post
    button_manage_branch_post = tk.Button(
        root, text=messages["manage_branch_post"], command=lambda: None)
    button_manage_branch_post.pack(fill=tk.X)

    # Add standoff post
    button_add_standoff_post = tk.Button(
        root, text=messages["add_standoff_post"], command=lambda: None)
    button_add_standoff_post.pack(fill=tk.X)

    # Manage standoff post
    button_manage_standoff_post = tk.Button(
        root, text=messages["manage_standoff_post"], command=lambda: None)
    button_manage_standoff_post.pack(fill=tk.X)

    # Select language
    button_select_language = tk.Button(
        root, text=messages["select_language"], command=lambda: on_select_language())
    button_select_language.pack(fill=tk.X)

    # Exit program
    button_exit = tk.Button(root, text=messages["exit"], command=root.quit)
    button_exit.pack(fill=tk.X)

    root.mainloop()


if __name__ == "__main__":
    main()
sys.exit(0)
