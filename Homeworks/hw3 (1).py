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
    def __init__(self, file='test.txt', size=5):
        
        #Create 5x5 game board
        self.size = size
        # Create window object
        self.window = Tk()
        self.window.title('Boggle')
        
        # Create canvas within the window
        self.canvas = Canvas(self.window, width = self.size * 20, height = self.size * 20, bg = 'white')
        self.readData(file)
        self.soln = []
        self.canvas.pack()
        # Draw the grid on the canvas
        self.clean()
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i * 20, j * 20, (i + 1) * 20, (j + 1) * 20)
                x = self.board[i][j]
                self.canvas.create_text(i * 20 + 10, j * 20 + 10, text = x)
        self.canvas.bind("<Button-1>", self.new)
        self.canvas.bind("<Button-2>", self.clean)
        self.canvas.bind("<Button-3>", self.extend)

        self.canvas.focus_set()
        
        # Start the main loop for the graphics
##################################################################################################################        
    def clean(self):
        weight = [ self.F[letter] for letter in ascii_lowercase]
        cumweight = [ sum(weight[:x+1]) for x in range(len(weight))]
        self.board = [choices(ascii_lowercase, cum_weights = cumweight, k = self.size) for x in range(self.size)]
##################################################################################################################
    def readData(self, file):
        # Read the file into the function and extract the words
        with open(file, 'r') as f:
            words = f.readlines()

        self.wordList = [i.strip() for i in words]
        letterList = []
        for word in self.wordList:
            for letter in word:
                letterList.append(''.join(letter))
        self.F = dict.fromkeys(ascii_lowercase, 0)
        total = 0
        for letter in letterList:
            total = total + 1
            if letter in self.F:
                self.F[letter] += 1
        
        for x in self.F:
            self.F[x] = self.F[x] / total
        print(self.F)
            
        # Build multi-layered dictionary data structure using letters as keys
        # and the inner-most value is the word itself
##################################################################################################################
        def trie(t):
            root = dict()
            branch = root
            for word in t:
                for letter in range(len(word)):
                    if letter == (len(word)-1):
                        branch[word[letter]] = word
                    else:
                        branch = branch.setdefault(word[letter], {})
                return root
            self.T = t(words)
##################################################################################################################
    # Solve recursively
    def ckSoln(self, soln):
        def ckPath(soln):
            path = []
            for x in range(len(soln)-1):
                if (soln[x][0] == soln[x+1][0] and (soln[i][1]+1 == soln[x+1][1] or soln[x][1]-1 == soln[x+1][1])) or (soln[x][1] == soln[x+1][1] and (soln[x][0]+1 == soln[x+1][0] or soln[x][0]-1 == soln[x+1][0])):
                    path.append(True)
                else:
                    path.append(False)
        if ckPath(soln) == True:
            keys = []
            for coord in soln:
                keys.append(self.board[coord[0]][coord[1]])
            T = self.T
            for key in keys:
                if key in T:
                    T = T[key]
                else:
                    return False
            return T
        else:
            return False
                
            
##################################################################################################################
    #Write a comment here you fuck
    def extend(self, event):
        path = []
        if len(soln) == 1:
            return True
        return (ckPath(all(path)))
    i = event.x //20
    j = event.y //20
    if (i,j) not in self.soln:
        self.soln.append((j,i))
        if ckSoln(self, soln) == True:
            if self.board[i][j] in self.T:
                self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill = 'green')
                self.T = self.T[self.board[i][j]]
                if len(self.soln) >= 3:
                    print("Congratulations, you found a word! Right-click to clear the board and search for more words; Or middle click to start a new game!")
            else:
                self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill = 'red')
                self.soln.pop()
        else:
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill = 'red')
            self.soln.pop()
    
    # Read through code from word net, othello
##################################################################################################################
    def new(self, event):
        self.canvas.focus_set()
        self.restart()
        self.reset()
        
##################################################################################################################
    def reset(self, event):
        self.canvas.create_rectangle(0, 0, 100, 100)
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i * 20, j * 20, (i + 1) * 20, (j + 1) * 20,)
                x = self.board[i][j]
                self.canvas.create_text(i * 20 + 10, j * 20 + 10, text = x)
        
        pass
##################################################################################################################
    def solve(self):
        # recursive
       # for i in range(len(size)):
           # for j in range(len(size)):
                # cannot go in direction such as (-1, 0) or (0, -1)
                # check if it is a legal position/path
        pass
