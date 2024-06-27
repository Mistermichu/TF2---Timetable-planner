import tkinter as tk
import tkinter.font as tkfont
import sys
import os


def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))
    from functions import get_language, load_messages, get_available_languages, PostList
    from linesection import create_block_section
    from posts import create_standoff_post

    languages = get_available_languages()
    post_list = PostList()

    def update_labels():
        button_add_block_section.config(text=messages["add_block_section"])
        button_manage_block_section.config(
            text=messages["manage_block_section"])
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

        selected_language = tk.StringVar()
        selected_language.set("en")

        for language_code in languages:
            language_button = tk.Button(
                language_window,
                text=language_code,
                command=lambda lc=language_code: choose_language(lc)
            )
            language_button.pack(fill=tk.X)

    messages = load_messages()

    root = tk.Tk()
    root.title(messages["title"])
    root.resizable(False, False)
    # Define column width
    columns_number = 3
    column_width = 50
    for column in range(columns_number):
        root.grid_columnconfigure(column, minsize=column_width)
    # Main Labels Fonts
    bold_font = tkfont.Font(weight="bold")

    #
    #
    #  Infrastructure column
    row_value = 0
    column_value = 0

    # Station
    label_station = tk.Label(root, text=messages["stations"], font=bold_font)
    label_station.grid(row=row_value, column=column_value)
    row_value += 1
    button_add_station = tk.Button(
        root, text=messages["add_station"], width=column_width, command=lambda: None)
    button_add_station.grid(row=row_value, column=column_value)
    row_value += 1
    button_manage_station = tk.Button(
        root, text=messages["manage_station"], width=column_width, command=lambda: None)
    button_manage_station.grid(row=row_value, column=column_value)
    row_value += 1

    # Standoff post
    label_standoff_post = tk.Label(
        root, text=messages["standoff_post"], font=bold_font)
    label_standoff_post.grid(row=row_value, column=column_value)
    row_value += 1
    button_add_standoff_post = tk.Button(
        root, text=messages["add_standoff_post"], width=column_width, command=lambda: create_standoff_post(root, messages, post_list))
    button_add_standoff_post.grid(row=row_value, column=column_value)
    row_value += 1
    button_manage_standoff_post = tk.Button(
        root, text=messages["manage_standoff_post"], width=column_width, command=lambda: None)
    button_manage_standoff_post.grid(row=row_value, column=column_value)
    row_value += 1

    # Branch post
    label_branch_post = tk.Label(
        root, text=messages["branch_post"], font=bold_font)
    label_branch_post.grid(row=row_value, column=column_value)
    row_value += 1
    button_add_branch_post = tk.Button(
        root, text=messages["add_branch_post"], width=column_width, command=lambda: None)
    button_add_branch_post.grid(row=row_value, column=column_value)
    row_value += 1
    button_manage_branch_post = tk.Button(
        root, text=messages["manage_branch_post"], width=column_width, command=lambda: None)
    button_manage_branch_post.grid(row=row_value, column=column_value)
    row_value += 1

    # Block section
    label_block_section = tk.Label(
        root, text=messages["block_section"], font=bold_font)
    label_block_section.grid(row=row_value, column=column_value)
    row_value += 1
    button_add_block_section = tk.Button(
        root, text=messages["add_block_section"], width=column_width, command=lambda: create_block_section(root, messages, post_list))
    button_add_block_section.grid(row=row_value, column=column_value)
    row_value += 1
    button_manage_block_section = tk.Button(
        root, text=messages["manage_block_section"], width=column_width, command=lambda: None)
    button_manage_block_section.grid(row=row_value, column=column_value)
    row_value += 1

    # Track line
    label_line = tk.Label(root, text=messages["track_line"], font=bold_font)
    label_line.grid(row=row_value, column=column_value)
    row_value += 1
    button_add_line = tk.Button(
        root, text=messages["add_line"], width=column_width, command=lambda: None)
    button_add_line.grid(row=row_value, column=column_value)
    row_value += 1
    button_manage_line = tk.Button(
        root, text=messages["manage_line"], width=column_width, command=lambda: None)
    button_manage_line.grid(row=row_value, column=column_value)
    row_value += 1

    #
    #
    # Other
    row_value = 0
    column_value = 2
    label_other_options = tk.Label(
        root, text=messages["other"], font=bold_font)
    label_other_options.grid(row=row_value, column=column_value)
    row_value += 1

    # Select language
    button_select_language = tk.Button(
        root, text=messages["select_language"], width=column_width, command=on_select_language)
    button_select_language.grid(row=row_value, column=column_value)
    row_value += 1

    # Exit program
    button_exit = tk.Button(
        root, text=messages["exit"], width=column_width, command=root.quit)
    button_exit.grid(row=row_value, column=column_value)

    root.mainloop()


if __name__ == "__main__":
    main()
sys.exit(0)
