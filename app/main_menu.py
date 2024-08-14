import tkinter as tk
import os
import glob
from functools import partial
import subprocess

def open_csv_viewer(file_path):

    subprocess.run(["python3", "match_ui.py", file_path])

def main():
    root = tk.Tk()
    root.title("Main Menu")
    data_folder = "../data"
    csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

    title_label = tk.Label(root, text="Select a CSV file to view:", font=('Arial', 14, 'bold'))
    title_label.pack(pady=10)

    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        button = tk.Button(root, text=file_name, command=partial(open_csv_viewer, file_path),
                           font=('Arial', 12), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
