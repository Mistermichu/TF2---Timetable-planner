# Stand-Off post requirements:
# a) Name

# Branch post requiremenst:
# a) Name

import tkinter as tk
from tkinter import messagebox


# Stand-Off post
def create_standoff_post(root, messages, post_list):

    def submit_standoff_post():
        type = "standoff"
        post_name = entry_standoff_post_name.get()
        post_list.add(post_name, type, messages)
        create_standoff_post_window.destroy()

    create_standoff_post_window = tk.Toplevel(root)
    create_standoff_post_window.title(messages["create_standoff_post"])
    create_standoff_post_window.resizable(False, False)

    row_value = 0
    # Add post name
    label_standoff_post_name = tk.Label(
        create_standoff_post_window, text=messages["add_standoff_post_name"])
    label_standoff_post_name.grid(row=row_value, column=0, sticky="w")
    entry_standoff_post_name = tk.Entry(create_standoff_post_window)
    entry_standoff_post_name.grid(row=row_value, column=1)

    row_value += 1

    # Submit changes
    row_value += 1
    button_submit = tk.Button(create_standoff_post_window,
                              text=messages["submit"], command=submit_standoff_post)
    button_submit.grid(row=row_value, column=1)
