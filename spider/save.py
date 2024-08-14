import csv
import os


def save_to_csv(data, filename='output.csv',directory=None):

    if directory:
        filepath = os.path.join(directory, filename)
    else:
        filepath = filename

    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
            ['Map', 'Player Name', 'Team Name', 'Hero Name', 'Rating', 'ACS', 'KDA', 'PM', 'KAST', 'ADR', 'HS', 'FK', 'FD',
             'FPM'])
        writer.writerows(data)