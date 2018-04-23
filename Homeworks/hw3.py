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
# Use tkinter to display graphical representation of the Boggle board
from string import ascii_lowercase
from random import choices
from tkinter import *

def hawkid():
    return(("dstutz",))

######################################################################
# Defaults to a Boggle board of size 5x5
class Boggle():
    def __init__(self, file='words.dat', size=5):
        # Create 5x5 game board
        self.size = size

        # Read in data file
        self.readData(file)

        # Set up board with random letters
        self.board = [choices(ascii_lowercase, cum_weights = self.counts, k = self.size * self.size)]
    
        # Create window object
        self.window = Tk()
        self.window.title('Boggle')

        # Create canvas within the window
        self.canvas = Canvas(self.window, width = self.size * 20, height = self.size * 20)
        self.canvas.pack()

        # Draw the grid on the canvas
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i * 20, j * 20, (i + 1) * 20, (j + 1) * 20)
                self.canvas.create_rectangle(i * 20 + 10, j * 20 + 10, text = self.board[i][j].pack())
        
        #mainloop
        self.mainloop()
    
    def readData(self, file):
        Trie = {}
        Freq = {}
        with open(file) as f:
            words = f.readlines()

        word = [x.strip() for x in words]
        
        def frequency(word, Freq):
            for x in word:
                if x not in Freq:
                    Freq[x] = 1
                else:
                    Freq[x] += 1
            for x in Freq:
                Freq[x] = Freq[x]/len(word)

        def trie(word, Trie):
            # base case
            if len(word) == 1:
                Trie[word[-1]] = word
                return(Trie)
                

            # recursive step
            if word[0] not in Trie.keys():
                Trie[word[0]] = {}
            return (trie(word[0], Trie[word[0]]))

    
    # solve recursively
    def ckSoln(self, soln):
        # return true if word is in the trie and false if otherwise
        # write method to find if the given path is legal with absolute value to see if the step between positions is 1
        if word in self.readData.Trie:
            return(True)
        else:
            return(False)
        def helper(soln):
            
            
            
        pass
    def extend(self, event):
        pass

    # Read through code from word net, othello
    def new(self, event):
        pass
    def reset(self, event):
        pass
    def solve(self):
        # recursive
       # for i in range(len(size)):
            #for j in range(len(size)):
               # cannot go in direction such as (-1, 0) or (0, -1)
                # check if it is a legal position/path
        pass
