from utils import *
import csv


if __name__ == "__main__":
    filename = input("Datafile name (without extension): ") + ".csv"
    
    with open(filename, 'a', encoding="utf-8", newline='') as file:
        w = csv.writer(file)
        url = input("Type in URL of player: ")
        all_stats = getStats(url) # stat values
        w.writerow(all_stats)

    
