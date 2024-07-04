import requests
from bs4 import BeautifulSoup
import csv
from main import *

if __name__ == "__main__":
    randomURL = "https://renderz.app/24/player/30901310" # this is just for header (it doenst really matter who it is)
    header = getLabels(randomURL) # labels

    filename = input("Datafile name (without extension): ") + ".csv"
    # write the header first
    with open(filename, 'w', encoding="utf-8", newline='') as file:
        w = csv.writer(file)
        w.writerow(header)