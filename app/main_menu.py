import tkinter as tk
import os
import glob
from functools import partial
import subprocess

def open_csv_viewer(file_path):
    subprocess.run(["python3", "match_ui.py", file_path])

def format_filename(file_name):
    base_name = file_name.split("-valorant")[0]
    teams = base_name.split("-vs-")
    if len(teams) == 2:
        return teams[0].replace("-", " "), "vs", teams[1].replace("-", " ")
    else:
        return base_name, "", ""

def create_team_button(root, team1, vs, team2, command):
    button_frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
    button_frame.pack(pady=5, padx=10, fill=tk.X)

    team1_label = tk.Label(button_frame, text=team1, font=('Arial', 12, 'bold'), anchor="center")
    team1_label.pack(side=tk.TOP, pady=(5, 0))

    vs_label = tk.Label(button_frame, text=vs, font=('Arial', 10), anchor="center")
    vs_label.pack(side=tk.TOP)

    team2_label = tk.Label(button_frame, text=team2, font=('Arial', 12, 'bold'), anchor="center")
    team2_label.pack(side=tk.TOP, pady=(0, 5))

    button_frame.bind("<Button-1>", lambda e: command())
    team1_label.bind("<Button-1>", lambda e: command())
    vs_label.bind("<Button-1>", lambda e: command())
    team2_label.bind("<Button-1>", lambda e: command())

def main():
    root = tk.Tk()
    root.title("Main Menu")

    data_folder = "../data/match_result_data"
    csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

    title_label = tk.Label(root, text="Select a Match to view:", font=('Arial', 14, 'bold'))
    title_label.pack(pady=10)

    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        team1, vs, team2 = format_filename(file_name)
        create_team_button(root, team1, vs, team2, partial(open_csv_viewer, file_path))
    root.mainloop()

if __name__ == "__main__":
    main()