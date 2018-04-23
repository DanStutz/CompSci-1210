#!/usr/local/anaconda/bin/python
######################################################################
# YOUR NAME GOES HERE
# YOUR DISCUSSION SECTION (e.g., "A09") GOES HERE
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
from random import randint
import numpy as np

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
      # Turn each row into a field/row dictionary and return dictionary while appending
        # dictionary to a list
    def helper():
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            d = {row[0] : tuple(row[1:-1]) for row in reader}
        pass
    dictList = []
    for row in reader:
        a = helper(row)
        print(a)
        for i in range (1, len(reader)):
            if row[l] != None:
                dictionary = {fields : values[row[i]]}
        dictList.append(dictionary)
    return dictList
######################################################################
# Write a good comment here.
def showPlot(D, field, values):
    import numpy as np
   
# data to plot
    n_groups = 4
    means_frank = (90, 55, 40, 65)
    means_guido = (85, 62, 54, 20)
 
# create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
 
    rects1 = plt.bar(index, means_frank, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Frank')
 
    rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Guido')
 
    plt.xlabel('Value')
    plt.ylabel('Percentage of population')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
    plt.legend()
     
    plt.tight_layout()
    plt.show()
    pass

######################################################################
# Write a good comment here.
def train(D, fields=fields, values=values):
    pass

######################################################################
# Write a good comment here.
def predict(example, P, fields=fields, values=values):
    pass

######################################################################
# Predict by guessing. You're going to be about half right!
def guess(example, fields=fields, values=values):
    return(values[0][randint(0,1)]==example['result'])

######################################################################
# Write a good comment here.
def test(D, P, fields=fields, values=values):
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


