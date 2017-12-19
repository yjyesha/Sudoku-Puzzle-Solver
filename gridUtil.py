import timeit
import copy

row = 'ABCDEFGHI'
col = '123456789'
val = []
rowL = []
colL = []
squareL = []

def fillValue(n,nums,b):
    nums[b] = n
    if len(n) == 1:
        val.append(nums.copy())
    return nums

def check(m, n):
    res = []
    for x in m:
        for y in n:
            res.append(x+y)
    return res
   

boxes = check(row,col)

for r in row:
    rowL.append(check(r,col))
for c in col:
    colL.append(check(row,c))

for rs in ('ABC','DEF','GHI'):
    for cs in ('123','456','789'):
        squareL.append(check(rs,cs))
    
uL = rowL + colL + squareL
us = dict((s, [u for u in uL if s in u]) for s in boxes)
neigh = dict((s, set(sum(us[s],[]))-set([s])) for s in boxes)





def addToGrid(grid):
    num = '123456789'
    v = []
    size = 0
    
    for d in grid:
        if d in num:
            v.append(d)
        if d == '-':
            v.append(num)
    size = len(v)
    assert size == 81
    return dict(zip(boxes,v))



def eliminate(v):
    curVal = [b for b in v.keys() if len(v[b]) == 1]
    for b in curVal:
        d = v[b]
        for p in neigh[b]:
            v[p] = v[p].replace(d,'')
    return v


def updateVal(v):
    for u in uL:
        for d in '123456789':
            dp = [b for b in u if d in v[b]]
            if len(dp) == 1:
                v[dp[0]] = d
    return v


def solveVal(v):
    sim = [b for b in v.keys() if len(v[b]) == 2]
    simL = []

    for b in sim:
        d = v[b]
        for p in neigh[b]:
            if d == v[p] and p != b:
                simL.append((b,p))

        if len(simL) == 0:
            return v

        for x,y in simL:
            if len(v[x]) != 2:
                return v
            dig1 = v[x][0]
            dig2 = v[x][1]

            if x[0] == y[0]:
                for r in rowL:
                    if x in r:
                        for n in r:
                            if dig1 in v[n] and x != n and y != n:
                                v[n] = v[n].replace(dig1,'')
                            if dig2 in v[n] and x != n and y != n:
                                v[n] = v[n].replace(dig2,'')


            if x[1] == y[1]:
                for c in colL:
                    if x in c:
                        for n in c:
                            if dig1 in v[n] and x != n and y != n:
                                v[n] = v[n].replace(dig1,'')
                            if dig2 in v[n] and x != n and y != n:
                                v[n] = v[n].replace(dig2,'')

            for s in squareL:
                if x in s and y in s:
                    for n in s:
                        if dig1 in v[n] and x != n and y != n:
                            v[n] = v[n].replace(dig1,'')
                        if dig2 in v[n] and x != n and y != n:
                            v[n] = v[n].replace(dig2,'')

    return v
                            
                    
            
           
def updatePuzzle(v):
    curVal = [b for b in v.keys() if len(v[b]) == 1]
    sol = False
    while not sol:
        prevVal = len([b for b in v.keys() if len(v[b]) == 1])
        v = eliminate(v)
        v = solveVal(v)
        v = updateVal(v)
        nextVal =  len([b for b in v.keys() if len(v[b]) == 1])

        sol = prevVal == nextVal
        if len([b for b in v.keys() if len(v[b]) == 0]):
            return False
    return v
    

    
