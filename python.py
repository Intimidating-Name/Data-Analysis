import math
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import sys
import functools

def latest_number():
    bs = BeautifulSoup(requests.get("https://m.xkcd.com/").content, 'html.parser').select("a")
    prevNumber = int(re.findall(r'/(\d{4})/', bs[1].prettify())[0])
    return prevNumber + 1

def latest_in_file():
    with open("altTextsBinary", mode="rb") as f:
        fileContent = f.read()
        fileStr = fileContent.decode('utf-8')
        fileList = fileStr.split("\n")
        numLines = len(fileList)
    if numLines > 404:
        return numLines
    else:
        return numLines - 1

def get_data_binary():
    soups = []
    for i in range(latest_in_file() + 1, latest_number() + 1):
        if i == 404:
            continue
        try:
            soups.append(BeautifulSoup(requests.get(f"https://m.xkcd.com/{i}/").content, 'html.parser').find(id="altText").get_text())
            if i % 100 == 0:
                print(i)
                with open("altTextsBinary", mode="ab") as f:
                    for message in soups:
                        f.write(str.encode(message + "\n"))
                soups = []
                time.sleep(1)
        except:
            print(i)
            print(message)
            sys.exit(0)

    with open("altTextsBinary", mode="ab") as f:
        for message in soups:
            f.write(str.encode(message + "\n"))
    
    print("done")

def get_frequencies(first):
    with open(first, mode="rb") as f:
        fileContent = f.read()
        fileStr = fileContent.decode('utf-8')
        lines = fileStr.split("\n")
    words = (" ".join(lines[:-1])).split(" ")
    sum = float(len(words))
    words = map(lambda x : x.strip("""!"#$%&'()*,-./:;?@[]_"""), words)
    freq = {}
    for i in words:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = {k:(float(v) / sum) for k, v in freq.items()}
    return freq

def get_word_frequencies(second):
    with open(second, mode="r") as f:
        fileContent = f.read()
        fileList = fileContent.split("\n")
        fileList = fileList[1:-1]
        freq = {}
        for i in fileList:
            line = i.split(",")
            freq[line[0]] = int(line[1])
    sum = float(functools.reduce(lambda x, y : x + y, freq.values()))
    freq = {k:(float(v) / sum) for k, v in freq.items()}
    return freq

def get_differences(first, second):
    "first - second = difference"
    "randall - english = difference"
    randall = get_frequencies(first)
    english = get_word_frequencies(second)
    difference = {}
    for k, v in randall.items():
        if k.lower() in english:
            difference[k] = (float(v) / float(english[k.lower()])) - 1
        elif k in english:
            difference[k] = (float(v) / float(english[k])) - 1
        else:
            difference[k] = float('inf')
    print({k:v for k, v in difference.items() if v > 17})
    return difference

def basic_table(first, second):
    freq = get_differences(first, second)
    keys = []
    values = []
    for k, v in freq.items():
        keys.append(k)
        values.append(v)
    printout = pd.DataFrame({"words":keys, "differences":values})
    print(printout)


def main():
    get_differences("altTextsBinary", "unigram_freq.csv")

if __name__ == "__main__":
    main()


#possible idea: find differences between frequencies of words in the alt text and their frequencies in the english language (lookup for database)
#other possible idea: find frequencies of all characters to find the ideal mapping for randall's keyboard

#other crazy idea: just scrape a sequence of random numbers and then do operations on that identical to what someone else does
#do this as a way to see whether their conclusions would look any different if their dataset was just random, like college admissions or smthng

















#emails = re.findall(r'"mailto:(\w+@\w+.\w{2,})"', str(links))

#seven_day = soup.find(id="seven-day-forecast")
#forecast_items = seven_day.find_all(class_="tombstone-container")
#tonight = forecast_items[0]
#
#
#period = tonight.find(class_="period-name").get_text()
#short_desc = tonight.find(class_="short-desc").get_text()
#temp = tonight.find(class_="temp").get_text()
#print(period)
#print(short_desc)
#print(temp)
#
#img = tonight.find("img")
#desc = img['title']
##print(desc)
#
#period_tags = seven_day.select(".tombstone-container .period-name")
#periods = [pt.get_text() for pt in period_tags]
#short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container.short-desc")]
#temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
#descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

