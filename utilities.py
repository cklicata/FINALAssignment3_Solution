#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computational Thinking Final Project

@author: charlotte komrosky-licata, eric jones

"""
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import operator
import csv

'''Function#1: Count of Movies and TV Shows Released Over 80 Years'''

def getCountofDates():
    dict = {'show_id': str, 'type': str, 'country': str, 'date_added': str, 'release_year': str, 'rating': str, 'duration': str, 'listed_in': str}
    df = pd.read_csv('Netflix_Titles.csv', index_col=0, dtype=dict)
    
    # Add column for movie type
    for i, row in df.iterrows():
        df.loc[i,"Dates"] = row["release_year"]

    # Get count of movies and TV shows
    datesdict = {}

    for row in df["Dates"]:
        if row in datesdict:
            datesdict[row] = datesdict[row]+1
        else:
            datesdict[row] = 1

    datesdict.pop('date_added', None)

    
    # create dataset of counts for barplot
    mylist = datesdict.items()
    mylist = sorted(mylist)
    print(mylist)
    x,y = zip(*mylist)

      
    fig = plt.figure(figsize = (12, 5))
     
    # create bar plot and save as png file
    plt.plot(x, y)

    plt.xlabel("Release Year")
    plt.ylabel("Count of Movies/TV Shows Released This Year")
    plt.title("Number of Movies and TV Shows Released Over 80 Years")
    plt.tick_params(axis='x', labelsize=8)
    plt.xticks(rotation=90)
    plt.savefig('datesplot.png', dpi = 100)
    plt.show()   # Note, this must be second since it clears plot


'''Function #2: Count of Total Movies and TV Shows'''

def getCountMoviesTV():
    dict = {'show_id': str, 'type': str, 'country': str, 'date_added': str, 'release_year': str, 'rating': str, 'duration': str, 'listed_in': str}
    df = pd.read_csv('Netflix_Titles.csv', index_col=0, dtype=dict)
    
    # Add column for movie type
    for i, row in df.iterrows():
        df.loc[i,"Movie Type"] = row["type"]

    # Get count of movies and TV shows
    typedict = {}

    for row in df["Movie Type"]:
        if row in typedict:
            typedict[row] = typedict[row]+1
        else:
            typedict[row] = 1

    typedict.pop('type', None)

    dict_pairs = typedict.items()
    pairs_iterator = iter(dict_pairs)
    first_pair = next(pairs_iterator)
    type1 = first_pair[0]
    count = first_pair[1]
    second_pair = next(pairs_iterator)
    type2 = second_pair[0]
    count2 = second_pair[1]
    

    # create dataset of counts for barplot
    data = {type1: count, type2: count2}
    courses = list(data.keys())
    values = list(data.values())
      
    fig = plt.figure(figsize = (10, 5))
     
    # create plot and save as png file
    plt.bar(courses, values, color ='blue', width = 0.7)
     
    plt.xlabel("Media Type")
    plt.ylabel("Count of Movies/TV Shows")
    plt.title("Number of Movies and TV Shows")
    plt.savefig('moviestvcount.png', dpi = 100)
    #plt.show()

'''Function #3: Top Countries With the Most TV Shows and Movies Made'''


def getCountriesCount():

    fig = plt.figure(figsize = (10, 5))


    #create dictionary of countries and number of movies and movies and TV shows made there
    countrydict = {}

    with open('Netflix_Titles.csv', 'r') as obj:
        csv_reader = (csv.reader(obj, delimiter=','))

        for row in csv_reader:
            worm = row[2]
            if worm in countrydict:
                countrydict[worm] = countrydict[worm]+1
            else:
                countrydict[worm] = 1

    countrydict.pop('country', None)

    sorted_dict = dict(sorted(countrydict.items(),key=operator.itemgetter(1),reverse=True))
    sorted_dict = dict(itertools.islice(sorted_dict.items(), 10))

    #create pie chart
    beep = []
    leep = []

    for x,y in sorted_dict.items():
        beep.append(x)
        leep.append(y)

    # Plot
    plt.pie(leep, labels=beep, autopct='%1.2f%%')
    plt.axis('equal')

    # create pie plot and save as png file
    plt.title("Top Ten Countries Where Movies and TV Shows Are Made", y=1.08)
    fig = plt.gcf()
    plt.rcParams['font.size'] = 10.0
    plt.savefig('countrieschart.png', dpi = 100)
    #plt.show()

'''Function #4: TV Shows and Movies With Most Popular Ratings'''

def getRatingsCount():
    dict = {'show_id': str, 'type': str, 'country': str, 'date_added': str, 'release_year': str, 'rating': str, 'duration': str, 'listed_in': str}
    df = pd.read_csv('Netflix_Titles.csv', index_col=0, dtype=dict)
    
    # Add column for movie type
    for i, row in df.iterrows():
        df.loc[i,"Ratings"] = row["rating"]

    # Get count of movies and TV shows
    ratingsdict = {}

    for row in df["Ratings"]:
        if row in ratingsdict:
            ratingsdict[row] = ratingsdict[row]+1
        else:
            ratingsdict[row] = 1

    ratingsdict.pop('type', None)
    
    # create dataset of counts for barplot
    courses = list(ratingsdict.keys())
    values = list(ratingsdict.values())
      
    fig = plt.figure(figsize = (10, 5))
     
    # create bar plot and save as png file
    plt.bar(courses, values, color ='green', width = 0.7)
     
    plt.xlabel("Rating")
    plt.ylabel("Count of Movies/TV Shows with Rating")
    plt.title("Number of Movies and TV Shows and their Ratings")
    plt.savefig('ratingschart.png', dpi = 100)
    #plt.show()








