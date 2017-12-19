from gridUtil import *
from dfs import *
from printPuzzle import *

def solveSudoku(g):

    v = addToGrid(g)
    #print('\n  \t Adding Values to grid ... \n')
    v = dfsPuzzle(v)
    print('\n \t Solution : \n \n')
    gridDisplay(v)

def demo():
    print('\n \n \t Instructions \n ')
    print('\n \t * Enter Puzzle as a continuous string of 81 characters with - for blank cells \n')
    print('\n \t * Sample Puzzle -1      \n')
    print('\n \t * Difficulty Level : Hard \n')
    print('\n \t ---2---633----54-1--1--398--------9----538----3--------263--5--5-37----847---1---')
    sample = '---2---633----54-1--1--398--------9----538----3--------263--5--5-37----847---1---'
    solveSudoku(sample)
    print('\n \t * Sample Puzzle -2     \n')
    print('\n \t * Difficulty Level : Medium \n')
    print('\n \t -7--3---8--2----141-8--47---8---5-----78129-----4---8---56--3-972----6--6---4--7-')
    sample = '-7--3---8--2----141-8--47---8---5-----78129-----4---8---56--3-972----6--6---4--7-'
    solveSudoku(sample)
    print('\n \t * Sample Puzzle -3      \n')
    print('\n \t * Difficulty Level : Easy \n')
    print('\n \t -1---4-----68-5--15-37-19--8-4--7---------------3--6-9--15-82-46--4-31-----2---5-')
    sample = '-1---4-----68-5--15-37-19--8-4--7---------------3--6-9--15-82-46--4-31-----2---5-'
    solveSudoku(sample)
    

def play():
    g = input('\n \t Enter Puzzle as a continuous string of 81 characters \n \t')
    solveSudoku(g)
        
    


if __name__ == '__main__':
    print('\n \n \t ************************************************************************************* \n\n')
    print('\t \t \t \t  S U D O K U \n')
    
    print('\n \n \t ************************************************************************************* \n\n')

    choice = 0
    while choice !=3:
        print('\n \n \t ************************************************************************************* \n\n')
        print('\n \t 1. Demo \n ')
        print('\n \t 2. Play \n ')
        print('\n \t 3. Exit \n ')
        choice = input(' \t Choose... \n \t')
        print('\n')
        if choice == '1':
            demo()
        elif choice == '2':
            play()
        else:
            break
              
          

