from gridUtil import *
from printPuzzle import *
import timeit
import copy

def dfsPuzzle(v):
    start = timeit.default_timer()
    g = search(v)
    stop = timeit.default_timer()
    t = stop - start
    print('\n \t Time DFS :  ', t,'\n \n')
    return g
  
def search(v):
    v = updatePuzzle(v)
    boxes = check('ABCDEFGHI','123456789')
    
    if v is False:
        return False
    if all(len(v[s]) == 1 for s in boxes):
        return v
    
    s = 'To find'
    p = {}
    
    for b in boxes:
        p[b] = len(v[b])

    for i in range(2,10):
        found = 0
        for j in p:
            if(p[j] == i):
                s = j
                found = 1
                break
        if found == 1:
            break

    sudokus = []

    for j in range(len(v[s])):
        d2 = copy.deepcopy(v)
        sudokus.append(d2)

    c = 0

    for d in v[s]:

        sudokus[c][s] = d
        fillValue(d,v,s)
        c = c + 1

    for x in sudokus:
        updatedSudoku = copy.deepcopy(x)
        a = search(updatedSudoku)

        if a:
            return a
        
    
    
