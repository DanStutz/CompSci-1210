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
        self.canvas.pack()
        # Draw the grid on the canvas
        self.clean()
        self.soln = []
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i * 20, j * 20, (i + 1) * 20, (j + 1) * 20)
                x = self.board[i][j]
                self.canvas.create_text(i * 20 + 10, j * 20 + 10, text = x)
        self.canvas.bind("<Button-1>", self.extend)
        self.canvas.bind("<Button-2>", self.new)
        self.canvas.bind("<Button-3>", self.reset)

        self.canvas.focus_set()
        
        # Start the main loop for the graphics
        

#################################################################################################################
    def readData(self, file):
        # Read the file into the function and extract the words
        with open(file, 'r') as f:
            wordList = []
            letterList = []
            for word in f:
                wordList.append(word.rstrip('\n'))
                for letter in word:
                    letterList.append(''.join(letter))
            for i in letterList:
                if i == '\n':
                    letterList.remove(i)
            print(wordList)
            print(letterList)
        
            self.F = dict.fromkeys(ascii_lowercase, 0)
            total = 0
            for letter in letterList:
                total = total + 1
                if letter in self.F:
                    self.F[letter] += 1
            print(self.F)
        for x in self.F:
            self.F[x] = self.F[x] / total
        
            
        # Build multi-layered dictionary data structure using letters as keys
        # and the inner-most value is the word itself
##################################################################################################################
        def trie(t):
            root = dict()
            for word in t:
                branch = root
                for letter in range(len(word)):
                    if letter == (len(word)-1):
                        branch[word[letter]] = word
                    else:
                        branch = branch.setdefault(word[letter], {})
           # print(root)
            return root
            
        self.T = trie(wordList)
##################################################################################################################
    def ckPath(self, soln):
        path = []
        if len(soln) == 1:
            return (True)
        for x in range(len(soln)-1):
            if (soln[x][0] == soln[x+1][0] and (soln[x][1]+1 == soln[x+1][1] or soln[x][1]-1 == soln[x+1][1])) or (soln[x][1] == soln[x+1][1] and (soln[x][0]+1 == soln[x+1][0] or soln[x][0]-1 == soln[x+1][0])):
                path.append(True)
            else:
                path.append(False)
        return (all(path))
##################################################################################################################
    def ckSoln(self, soln):
        if self.ckPath(soln) == False:
            return False
        letters = []
        for x in  soln:
            letters.append(self.board[x[1]][x[0]])
        p_dict = self.T.get(letters[0])
        for y in range(1, len(letters)):
            if p_dict == None:
                return(False)
            elif type(p_dict.get(letters[y])) == str:
                if p_dict.get(letters[y]) == "".join(letters):
                    return(p_dict.get(letters[y]))
            elif type(p_dict.get(letters[y])) == dict:
                p_dict = p_dict.get(letters[y])
        return(p_dict)
                   
            
##################################################################################################################
    #Write a comment here you fuck
    def extend(self, event):
        i = event.x // 20
        j = event.y // 20
        self.soln.append((j,i))
        print((j,i))
        if self.ckPath(self.soln) == False:
            self.soln.pop()
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill = 'red')
            self.canvas.create_text((i+5)*20, (j+5)*20, text = self.board[i][j])
            return False
    
        elif type(self.ckPath(self.soln)) == dict:
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill = 'green')
            self.canvas.create_text(i*20+10, j*20+10, text = self.board[i][j])
            return True
        elif type(self.ckPath(self.soln)) == str:
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill = 'green')
            self.canvas.create_text(i*20+10, j*20+10, text = self.board[i][j])
            print('You found a word! Right click to find more words on this board or middle click to create a new board.')
            self.reset()
            
    
    # Read through code from word net, othello
##################################################################################################################        
    def clean(self):
        self.canvas.focus_set()
        weight = [self.F[letter] for letter in ascii_lowercase]
        cumweight = [ sum(weight[:x+1]) for x in range(len(weight))]
        self.board = [choices(ascii_lowercase, cum_weights = cumweight, k = self.size) for x in range(self.size)]
#################################################################################################################
    def new(self, event = "<Button-2>"):
        self.canvas.focus_set()
        self.clean()
        self.reset()
        
        
##################################################################################################################
    def reset(self, event="<Button-3>"):
        self.canvas.focus_set()
        self.canvas.create_rectangle(0, 0, 100, 100, fill ='white')
        for i in range(self.size):
            for j in range(self.size):
                x = self.board[i][j]
                self.canvas.create_rectangle(i*20, j*20, (i + 1)*20, (j + 1)*20)
                self.canvas.create_text(i*20+10, j*20 + 10, text = x)
        if self.soln != []:
            self.soln = []
        
##################################################################################################################
    def solve(self):
        # recursive
       # for i in range(len(size)):
           # for j in range(len(size)):
                # cannot go in direction such as (-1, 0) or (0, -1)
                # check if it is a legal position/path
        pass
