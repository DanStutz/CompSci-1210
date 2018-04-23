#!/usr/local/anaconda/bin/python
######################################################################
# Daniel Stutz
# A08
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number. 
#
# Failure to correctly do so will result in a 0 grade.
######################################################################
def hawkid():
    return(("dstutz",))

######################################################################
import csv
import matplotlib.pyplot as plt
import numpy as np
from random import randint


# Fields from the input file, in same order as they appear in the file
# (ignoring respondent ID). Do not modify or change.
fields=['result','smoke','drink','gamble','skydive','speed','cheat','steak','cook','gender','age','income','education','location']
# Corresponding field values from the input file. Do not modify or change.
values=[('lottery a','lottery b'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),
        ('rare','medium rare','medium','medium well','well'),('male','female'),
        ('18-29','30-44','45-60','> 60'),
        ('$0 - $24,999','$25,000 - $49,999','$50,000 - $99,999','$100,000 - $149,999','$150,000+'),
        ('less than high school degree','high school degree','some college or associate degree','bachelor degree','graduate degree'),
        ('east north central','east south central','middle atlantic','mountain','new england','pacific',
         'south atlantic','west north central','west south central')]

######################################################################
# Write a good comment here.
def readData(filename='steak-risk-survey.csv', fields=fields, values=values):
    nList = [] #List of data returned from the helper function
    def helper(row):
        nDict = {}
        for x in range(len(fields)):
            if row[x+1] != '' :
                nDict[fields[x]]=row[x+1].lower()
        return nDict
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if row[1].lower() in values[0]:
                nList.append(helper(row))
    return nList
######################################################################
# Write a good comment here.
def showPlot(D, field, values):
    lotA = {a:0 for a in values}
    lotB = {a:0 for a in values}
    for row in D:
        if row['result'] == 'lottery a':
            if field in row:
                lotA[row[field]] += 1

        elif row['result'] == 'lottery b':
            if field in row:
                lotB[row[field]] += 1
    sumlotA = sum(lotA.values())
    sumlotB = sum(lotB.values())
   
    
    listA = list(lotA.values())
    listB = list(lotB.values())
    
    for i in range(len(listA)):
        listA[i] = listA[i] / float(sumlotA + sumlotB)
        listB[i] = listB[i] / float(sumlotA + sumlotB)

    fig, ax = plt.subplots()
    
    bar_width = 0.35
    opacity = 0.8

    indexLA = [i for i in range(len(listA))]
    indexLB = [i + bar_width for i in range(len(listB))]
    rectsLA = plt.bar(indexLA, listA, bar_width, alpha = opacity, color = 'b', label = 'Lottery A', align='center')
    rects2 = plt.bar(indexLB, listB, bar_width, alpha = opacity, color = 'r', label = 'Lottery B', align='center')
    plt.xlabel('Value')
    plt.ylabel('Percentage of population')
    plt.title('Lottery preference by "' + field + '"')
    plt.xticks(indexLB, values)
    plt.legend()
    plt.tight_layout()
    plt.show()
    

######################################################################
# Write a good comment here.
def train(D, fields=fields, values=values):
    P = {}

    for x in range(len(fields)):
        P[fields[x]] = {}
        for row in D:
            for r in values[x]:
                P[fields[x]][row['result']] = {}
                for value in values[x]:
                    P[fields[x]][row['result']][value] = 0
    for row in D:
        for field in fields:
            if field in row:
                P[field][row['result']][row[field]] += 1


    
    print(P)

    return(P)
######################################################################
# Write a good comment here.
def predict(example, P, fields=fields, values=values):
    lotA = P['result']['lottery a']
    lotB = P['result']['lottery b']

    # Calculate the probabilities for both lottery a and lottery b
    for i in range(len(fields)):
        for v in lotA.values():
            if 'result' in example:
                lotA[v] = lotA[v] * P[fields[i]]['lottery a'][example[fields[i]]]
                lotB[v] = lotB[v] * P[fields[i]]['lottery b'][example[fields[i]]]

                if lotA[v] > lotB[v]:
                    return('lottery a')
                elif lotB[v] > lotA[v]:
                    return('lottery b')
    pass

######################################################################
# Predict by guessing. You're going to be about half right!
def guess(example, fields=fields, values=values):
    return(values[0][randint(0,1)]==example['result'])

######################################################################
# Write a good comment here.
def test(D, P, fields=fields, values=values):
    count = 0

    # Iterate through the examples in D
    for row in D:

        # Compare the prediction of classifier P with the actual value
        # of the lottery that they chose
        if predict(D, P) == D[row['result']]:
            count += 1

    percentage = count / len(D)

    return(percentage)
    pass

######################################################################
# Fisher-Yates-Knuth fair shuffle, modified to only shuffle the last k
# elements. S[-k:] will then be the test set and S[:-k] will be the
# training set.
def shuffle(D, k):
    # Work backwards, randomly selecting an element from the head of
    # the list and swapping it into the tail location. We don't care
    # about the ordering of the training examples (first len(D)-N),
    # just the random selection of the test examples (last N).
    i = len(D)-1
    while i >= len(D)-k:
        j = randint(0, i)
        D[i], D[j] = D[j], D[i]
        i = i-1
    return(D)

# Evaluate.
def evaluate(filename='steak-risk-survey.csv', fields=fields, values=values, trials=100):
    # Read in the data.
    D = readData(filename, fields, values)
    # Establish size of test set (10% of total examples available).
    N = len(D)//10
    result = 0
    random = 0
    for i in range(trials):
        # Shuffle to randomly select N test examples.
        D = shuffle(D, N)
        # Train the system on first 90% of the examples.
        P = train(D[:-N], fields=fields, values=values)
        # Test on last 10% of examples, chosen at random by shuffle().
        result += test(D[-N:], P, fields=fields, values=values)
        # How well would you do guessing at random?
        random += sum([ len([ True for x in D[-N:] if guess(x)])/N ])
    # Return average accuracy.
    print('NaiveBayes={}, random guessing={}'.format(result/trials, random/trials))


