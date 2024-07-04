import requests
from bs4 import BeautifulSoup
import csv



def format_labels(bsTagList): # wow this way sucks but it still works
    # input bsTagList is list of Tags: <span class="player-stat-name svelte-1nsass1">Pace</span> (need to stringify it first)
    # output is string "Pace"
    stringList = []

    for bsTag in bsTagList:
        taglen = len('<span class="player-stat-name svelte-1nsass1">')
        endtaglen = len('</span>')
        string = str(bsTag)

        stringList.append(string[taglen:len(string)-endtaglen].strip())

    return stringList

def format_stats(bsTagList): 
    # input bsTagList is list of Tags: <span class="player-stat-value stat-color-great svelte-1nsass1">103</span> (need to stringify it first)
    # output is number 103
    intList = []

    for bsTag in bsTagList:
        string = str(bsTag)

        # finding where > starts to locate the number value
        index = 0
        for char in string:
            if char == '>':
                break
            index += 1

        endtaglen = len('</span>')
        newString = string[index+1 : len(string) - endtaglen]
        intList.append(int(newString))

    return intList

def format_others(bsTagList, prefs):
    # prefs is liek [0, 4, 5, 6, 7, 8]
    # which characteristics u want
    
    stringList = []
    i = 0

    for bsTag in bsTagList:
        if i in prefs:
            string = str(bsTag)

            # finding where > starts to locate the number value
            index = 0
            for char in string:
                if char == '>':
                    break
                index += 1

            endtaglen = len('</span>')
            newString = string[index+1 : len(string) - endtaglen]
            stringList.append(newString)
        i += 1

    return stringList

def getLabels(url): # sets up and extracts all the labels
    # takes a URL link
    # returns a list with all the labels
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # extracting all the data and putting it into a dictionary
    taglabels = soup.find_all('span', class_='player-stat-name')
    labels = format_labels(taglabels) # convert into strings and just the labels
   

    otherlabels = soup.find_all('span', class_='text-white font-semibold')
    morelabels = format_others(otherlabels, [0+1, 4+1, 5+1, 6+1, 7+1, 8+1])
    morelabels = ["NAME"] + morelabels

    all_labels = morelabels + labels
    return all_labels

def getStats(url):
    # takes a URL link
    # returns a list with all the stat values
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    statlabels = soup.find_all('span', class_='player-stat-value')
    stats = format_stats(statlabels) # convert into numbers and just the stat values

    otherstats = soup.find_all('span', class_='text-white/40')
    morestats = format_others(otherstats, [0, 4, 5, 6, 7, 8])

    name = str(soup.find('span', class_='text-white font-semibold'))
    index = 0
    for char in name:
        if char == '>':
            break
        index += 1

    endtaglen = len('</span>')
    playername = name[index+1 : len(name) - endtaglen]
    morestats = [playername] + morestats

    all_stats = morestats + stats
    return all_stats

if __name__ == "__main__":
    url = "https://renderz.app/24/player/30901310"
    header = getLabels(url) # labels, stat values
    all_stats = getStats(url) # labels, stat values

    # with open("penis.csv", 'w') as file:
    #     w = csv.writer(file)
    #     w.writerow(header)

    

    # print(header)
    # print(all_stats)
    
