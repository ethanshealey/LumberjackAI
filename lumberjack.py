'''
Ethan Shealey

NOTE: ~ = Player and Tree in square
      x = Trees remaining in square
      o = Player standing in square (no trees)
'''
import random
import time
from os import system, name

'''
Trees
'''
tree1 = True
tree2 = True
tree3 = True
tree4 = True

'''
Seed Random
'''
random.seed()

'''
Clear screen function
'''
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

'''
lumberjack object
'''
class lumberjack:
    def __init__(self):
        # Initialize needed variabes
        self.location = 3
        self.score = 0
        self.moves = 0
        self.numOfTrees1 = random.randint(5,10)
        self.numOfTrees2 = random.randint(5,10)
        self.numOfTrees3 = random.randint(5,10)
        self.numOfTrees4 = random.randint(5,10)

    def printBoard(self):
        # Print the game board
        global tree1, tree2, tree3, tree4
        print('   _   ')
        print(' _|%c|_ '   % ('~' if tree1 and self.location == 1 else 'x' if tree1 else 'o' if self.location==1 else ' '))
        print('|%c %c %c|' % ('~' if tree2 and self.location == 2 else 'x' if tree2 else 'o' if self.location==2 else ' ',\
                              'o' if self.location==3 else ' ',\
                              '~' if tree3 and self.location == 4 else 'x' if tree3 else 'o' if self.location==4 else ' '))
        print(' ‾|%c|‾'    % ('~' if tree4 and self.location == 5 else 'x' if tree4 else 'o' if self.location==5 else ' '))
        print('   ‾   ')
        print('Trees left:', self.numOfTrees1+self.numOfTrees2+self.numOfTrees3+self.numOfTrees4)

    def chop(self):
        global tree1, tree2, tree3, tree4
        # If in box 1
        if self.location == 1:
            if tree1:
                self.numOfTrees1 -= 1
                self.score += 1
                if self.numOfTrees1 == 0:
                    tree1 = False
        # If in box 2
        elif self.location == 2:
            if tree2:
                self.numOfTrees2 -= 1
                self.score += 1
                if self.numOfTrees2 == 0:
                    tree2 = False
        # If in box 3
        elif self.location == 3:
            pass
        # If in box 4
        elif self.location == 4:
            if tree3:
                self.numOfTrees3 -= 1
                self.score += 1
                if self.numOfTrees3 == 0:
                    tree3 = False
        # If in box 5
        elif self.location == 5:
            if tree4:
                self.numOfTrees4 -= 1
                self.score += 1
                if self.numOfTrees4 == 0:
                    tree4 = False

    '''
    Move player north if possible
    '''
    def goNorth(self):
        print('Player goes North')
        if self.location == 1 or self.location == 2 or self.location == 4:
            pass
        else:
            self.location -= 2

    '''
    Move player east if possible
    '''
    def goEast(self):
        print('Player goes East')
        if self.location == 1 or self.location == 4 or self.location == 5:
            pass
        else:
            self.location += 1

    '''
    Move player south if possible
    '''
    def goSouth(self):
        print('Player goes South')
        if self.location == 2 or self.location == 4 or self.location == 5:
            pass
        else:
            self.location += 2

    '''
    Move player west if possible
    '''
    def goWest(self):
        print('Player goes West')
        if self.location == 1 or self.location == 2 or self.location == 5:
            pass
        else:
            self.location -= 1

# Create lumberjack instance
player = lumberjack()
clear()
print('Player Spawns')
# Print base game
player.printBoard()
time.sleep(.5)

# While there are still trees remaining
while tree1 or tree2 or tree3 or tree4:
    clear()
    # Choose random direction 
    direction = random.randint(1, 4)
    # Increment how many times the player has moved
    player.moves += 1
    # Go North
    if direction == 1:
        player.goNorth()
        player.chop()
    # Go East
    elif direction == 2:
        player.goEast()
        player.chop()
    # Go South
    elif direction == 3:
        player.goSouth()
        player.chop()
    # Go West
    elif direction == 4:
        player.goWest()
        player.chop()

    # Print updated game
    player.printBoard()
    time.sleep(.5)

# Print player's final score and total moves
print('Score: ', player.score, '\nMoves: ', player.moves)