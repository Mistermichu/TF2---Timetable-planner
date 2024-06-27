# Line section is a part of a track line between specific points, eg.: Station and stand-off post. This can be later added to create track line.
# Line section must contain:
# Specific track details as:
# a) speed limit
# b) electrification status
# c) hours and availability
# d) starting point
# e) ending point

import sys
import os
import tkinter as tk
from tkinter import ttk


def create_line_section(root, messages, post_list):

    def submit_create_line_section():
        sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))
        from functions import generate_timetable, check_new_file

        folder_name = "line sections"
        line_section_name = str(entry_line_section_name.get())
        track_number = 1

        try:
            speed_limit = int(entry_speed_limit.get())
            speed_limit = str(speed_limit)
        except ValueError:
            from tkinter import messagebox
            messagebox.showerror(
                messages["error"], messages["incorrect_value"])
            create_line_section_window.destroy()
            return

        line_section_data = {
            "track_number": track_number,
            "starting_point": entry_starting_point.get(),
            "ending_point": entry_ending_point.get(),
            "speed_limit": speed_limit,
            "electrification_status": var_electrification_status.get(),
            "time_table": generate_timetable()
        }

        check_new_file(folder_name=folder_name, file_name=line_section_name,
                       file_data=line_section_data, messages=messages)

        create_line_section_window.destroy()

    create_line_section_window = tk.Toplevel(root)
    create_line_section_window.title(messages["create_line_section"])
    create_line_section_window.resizable(False, False)

    row_value = 0
    # Add line section name
    label_line_section_name = tk.Label(
        create_line_section_window, text=messages["line_section_name"])
    label_line_section_name.grid(row=row_value, column=0, sticky="W")
    entry_line_section_name = tk.Entry(create_line_section_window)
    entry_line_section_name.grid(row=row_value, column=1)

    row_value += 1

    # Add starting point
    label_starting_point = tk.Label(
        create_line_section_window, text=messages["starting_point"])
    label_starting_point.grid(row=row_value, column=0, sticky="w")
    entry_starting_point = ttk.Combobox(
        create_line_section_window, values=post_list.get_names())
    entry_starting_point.grid(row=row_value, column=1)

    row_value += 1

    # Add ending point
    label_ending_point = tk.Label(
        create_line_section_window, text=messages["ending_point"])
    label_ending_point.grid(row=row_value, column=0, sticky="w")
    entry_ending_point = ttk.Combobox(
        create_line_section_window, values=post_list.get_names())
    entry_ending_point.grid(row=row_value, column=1)

    row_value += 1

    # Add speed limit
    label_speed_limit = tk.Label(
        create_line_section_window, text=messages["speed_limit"])
    label_speed_limit.grid(row=row_value, column=0, sticky="W")
    entry_speed_limit = tk.Entry(create_line_section_window)
    entry_speed_limit.grid(row=row_value, column=1)
    label_units = tk.Label(create_line_section_window, text="km/h")
    label_units.grid(row=row_value, column=2)

    row_value += 1

    # Electrification status
    label_electrification_status = tk.Label(
        create_line_section_window, text=messages["electrified"])
    label_electrification_status.grid(row=row_value, column=0, sticky="W")
    var_electrification_status = tk.StringVar(value="No")
    radio_electrification_status_yes = tk.Radiobutton(
        create_line_section_window, text=messages["yes"], variable=var_electrification_status, value="Yes")
    radio_electrification_status_yes.grid(row=row_value, column=1)
    radio_electrification_status_no = tk.Radiobutton(
        create_line_section_window, text=messages["no"], variable=var_electrification_status, value="No")
    radio_electrification_status_no.grid(row=row_value, column=2)

    row_value += 1

    # Submit changes
    row_value += 1
    button_submit = tk.Button(create_line_section_window,
                              text=messages["submit"], command=submit_create_line_section)
    button_submit.grid(row=row_value, column=1)
