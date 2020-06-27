import markdown_table
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import common
import csv
import statistics

global headers

# return csv as data structure which maps {'state' : DataFrame } where the DataFrame has counties as rows and days as columns for the state
def get_data():
    data = {}
    global headers
    with open("data/time_series_covid_19_confirmed_US.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if ("UID") in row[0]:
                headers = row[11:]
            if "840" not in row[0]:
                continue
            state = row[6]
            if state in data:
                data[state].append(row[11:]) 
            else:
                data[state] = [row[11:]]
    for key in data:
        data[key] = pd.DataFrame(data[key], columns=headers)
        for column in data[key]:
            data[key][column] = pd.to_numeric(data[key][column])
    return data
    # make data frames out of the lists

# given a column header (a day) return the adjacent one (the next day)
def nextday(day):
    global headers
    for i in range(len(headers) - 1):
        if headers[i] == day:
            return headers[i+1]


    return day
# For each state determine the number of confirmed cases by day. This will require a calculation from day x minus day x−1.
def i(data, state, day):
    global headers 
    next_day = nextday(day)
    if day == headers[len(headers) - 1]:
        return 0
    return np.sum(data[state][next_day] - data[state][day])

# Calculate the maximum number of cases in any given day by state
def ii(data, state):
    confirmed = []
    for (day, columnData) in data[state].iteritems():
        confirmed.append(i(data, state, day))
    return max(confirmed)

#By state, once the first confirmed case is identified, calculate the mean from that point through June 7, 2020
def iii(data, state):
    started = False
    counts = []
    for (day, columnData) in data[state].iteritems():
        if np.sum(columnData) != 0:
            started = True
        if started == True:
            counts.append(i(data, state, day))
    return statistics.mean(counts)

def main():

    data = get_data()

    results = []
    for state in data.keys():
        results.append([state, str(ii(data, state)), str(iii(data, state))])
    
    print(markdown_table.render(["Results", "Max", "Average"], results) + "\n")

    


if __name__ == "__main__":
    main()






