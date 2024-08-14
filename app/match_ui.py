import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import os
import sys


def main(csv_file):
    root = tk.Tk()
    root.title(f"Match Statistics - {os.path.basename(csv_file)}")
    data = pd.read_csv(csv_file)

    maps = data['Map'].unique()
    map_data = {map_name: data[data['Map'] == map_name] for map_name in maps}

    def load_hero_images():
        hero_images = {}
        image_folder = '../img/hero_img'

        for hero_names in data['Hero Name']:
            heroes = hero_names.strip("[]").replace("'", "").split(", ")
            for hero_name in heroes:
                processed_name = hero_name.lower()
                image_path = os.path.join(image_folder, f"{processed_name}.png")
                if os.path.exists(image_path):
                    hero_images[hero_name] = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))

        return hero_images

    hero_images = load_hero_images()

    def update_table(selected_map):
        for widget in frame.winfo_children():
            widget.destroy()

        for col, header in enumerate(headers):
            header_label = ttk.Label(frame, text=header, font=('Arial', 10, 'bold'))
            header_label.grid(row=0, column=col, padx=5, pady=5)

        current_data = map_data[selected_map]
        team_switch_index = 5

        for row_index, row_data in current_data.iterrows():
            actual_row = row_index + 1
            if row_index == team_switch_index:
                for col in range(len(headers)):
                    empty_label = ttk.Label(frame, text="")
                    empty_label.grid(row=actual_row, column=col)
                actual_row += 1

            for col_index, header in enumerate(headers):
                value = row_data[header]
                if header == 'Hero Name':
                    image_frame = tk.Frame(frame)
                    image_frame.grid(row=actual_row, column=col_index, padx=5, pady=5)

                    heroes = value.strip("[]").replace("'", "").split(", ")
                    for hero_name in heroes:
                        if hero_name in hero_images:
                            image_label = tk.Label(image_frame, image=hero_images[hero_name])
                            image_label.pack(side=tk.LEFT)
                else:
                    color = 'black'
                    if header == 'KDA':
                        k, d, a = map(int, value.split('/'))
                        color = 'green' if k > d else 'red'
                    label = ttk.Label(frame, text=value, font=('Arial', 10), foreground=color)
                    label.grid(row=actual_row, column=col_index, padx=5, pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    for map_name in maps:
        button = tk.Button(button_frame, text=map_name, command=lambda mn=map_name: update_table(mn),
                           font=('Arial', 12), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        button.pack(side=tk.LEFT, padx=10)

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    headers = ["Player Name", "Team Name", "Hero Name", "Rating", "ACS", "KDA", "PM", "KAST", "ADR", "HS", "FK", "FD",
               "FPM"]

    update_table(maps[0])

    root.mainloop()


if __name__ == "__main__":
    csv_file = sys.argv[1]
    main(csv_file)