#!/usr/local/anaconda/bin/python
# Alberto Maria Segre
# CS:1210:0AAA

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.
from string import ascii_lowercase
from random import choices
from tkinter import *

######################################################################
# This function returns your hawkid for the autograder.
def hawkid():
    return(("segre",))

######################################################################
# This class definition is agnostic as to size, with the default being
# 5x5; the assignment allows for boards that are fixed at 5x5.
class Boggle ():
    def __init__(self, file='words.dat', size=5):
        '''Initialize a 5x5 (or otherwise specified) game board.'''
        self.size = size
        # Read in the word file; establishes self.trie and self.counts.
        self.readData(file)
        #return(None)

        # Create a window object of type Tk.
        self.window = Tk()
        self.window.title('Boggle')
        # Create a canvas within the window to draw on.
        self.canvas = Canvas(self.window, width = self.size*20, height = self.size*20, bg='white')
        self.canvas.pack()
        # Set up sizeXsize board with random letters.
        self.resetBoggle()
        # Draw the grid on the canvas.
        self.resetDisplay()
        # Bind left/middle/right button clicks to callback methods.
        self.canvas.bind("<Button-1>", self.extendPath)
        self.canvas.bind("<Button-2>", self.resetBoggle)
        self.canvas.bind("<Button-3>", self.resetDisplay)
        # Focus the mouse on the canvas.
        self.canvas.focus_set()

    def readData(self, filename):
        '''Reads in legal word file, establishing self.trie and self.counts as you go.'''
        # Recursive helper function builds trie and counts letters.
        def buildTrie(letters, trie, freq, word):
            # Increment letter count for this letter.
            freq[letters[0]] += 1
            # Last letter; add word to trie. Base case.
            if len(letters) == 1:
                trie[letters[0]] = word
                return()
            # Descend into trie recursively, adding new key if needed.
            if letters[0] not in trie.keys():
                trie[letters[0]] = {}
            # Recursive step.
            buildTrie(letters[1:],trie[letters[0]], freq, word)
        # Read in the words from specified file.
        with open (filename, 'r') as file:
            words = file.read().lower().split()
        # Contains frequencies of letters.
        freq = { k:0 for k in ascii_lowercase }
        # Contains trie of words.
        self.trie = {}
        # Process each word.
        for word in words:
            buildTrie(word, self.trie, freq, word)
        # Calculate cumulative letter counts for random distribution
        # of letters to board locations.
        weights = [ freq[l] for l in ascii_lowercase ]
        self.counts = [ sum(weights[:i+1]) for i in range(len(ascii_lowercase)) ]

    # A soln is a list of tuples corresponding to board positions.
    def ckSoln(self, soln):
        '''Checks that a solution is a word in the dictionary and that the letters are contiguous.'''
        # Helper function checks that a path is contiguous and unique.
        def ckPath(soln):
            if len(set(soln)) == len(soln):
                steps = [ sum([ abs(x-y) for x,y in zip(soln[i],soln[i-1]) ]) for i in range(1,len(soln)) ]
                return(len(soln)-1 == sum(steps))
        # Recursive helper function checks that word is in trie.
        def ckWord(soln, trie):
            if len(soln) == 1 and self.board[soln[0][0]][soln[0][1]] in trie:
                return(trie[self.board[soln[0][0]][soln[0][1]]])
            elif len(soln) <= 1 or self.board[soln[0][0]][soln[0][1]] not in trie:
                return(False)
            else:
                return(ckWord(soln[1:], trie[self.board[soln[0][0]][soln[0][1]]]))

        # Solution is good if it doesn't reuse letters, has a legal
        # trajectory, and leads to a word in the trie.
        if ckPath(soln):
            return(ckWord(soln, self.trie))

    # Find all solutions embedded in the puzzle.
    def solve(self):
        '''Return a list of all words found in the puzzle using findWords() at each board location.'''
        # Recursive helper function does the search guided by trie.
        def search(soln, trie):
            if not isinstance(trie, dict):
                # End of the road: return the solution found, which is
                # the word stored at the leaf of the trie.
                return([trie])
            # Still some trie left to traverse... 
            solns = []
            for x,y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                # soln[0] is the previous solution location (soln is maintained in reverse order).
                newloc = (soln[0][0]+x, soln[0][1]+y)
                # Keep searching if newloc is on board, not in soln so far, and letter at newloc is in trie.
                if all([ 0 <= loc < self.size for loc in newloc ]) and newloc not in soln and self.board[newloc[0]][newloc[1]] in trie.keys():
                   # Build up the solution (in reverse order).
                   solns.extend(search([newloc] + soln, trie[self.board[newloc[0]][newloc[1]]]))
            return(solns)
        # Initialize results list.
        results = []
        # Scan each board location.
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] in self.trie.keys():
                    # Extend results with words found starting at x,y.
                    results.extend(search([(x, y)],self.trie[self.board[x][y]]))
        return(results)

    # Bound to left mouse button: used to input self.soln.
    def extendPath(self, event):
        '''Handles left mouse button clicks, adding to user solution.'''
        i = event.x//20
        j = event.y//20
        # Add the current location.
        self.soln.append((i, j))
        if self.ckSoln(self.soln):
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill='green')
        else:
            self.canvas.create_oval(i*20+1, j*20+1, (i+1)*20-1, (j+1)*20-1, fill='red')
            # Remove what you added.
            self.soln = self.soln[:-1]
        self.canvas.create_text(i*20+10, j*20+10, text=self.board[i][j].upper())

    # Bound to center mouse button: creates a new puzzle.
    def resetBoggle(self, *args):
        '''Sets up a new board, initializes user solution, and updates display.'''
        self.board = [ choices(ascii_lowercase, cum_weights=self.counts, k=self.size) for i in range(self.size) ]
        self.soln = []
        self.resetDisplay()

    # Bound to right mouse button: clears display.
    def resetDisplay(self, *args):
        '''Updates the display, flushing any old markings.'''
        self.soln = []
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20, fill='white')
                self.canvas.create_text(i*20+10, j*20+10, text=self.board[i][j].upper())
        
