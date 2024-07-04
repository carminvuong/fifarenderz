from utils import *
import csv


if __name__ == "__main__":
    randomURL = "https://renderz.app/24/player/30901310" # this is just for header (it doenst really matter who it is)
    header = getLabels(randomURL) # labels

    # write the header first
    with open("data.csv", 'w', encoding="utf-8", newline='') as file:
        w = csv.writer(file)
        w.writerow(header)