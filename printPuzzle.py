from gridUtil import *





def gridDisplay(v):
    b = 1 + max(len(v[s]) for s in boxes)
    l = '|'.join(['*'*(b*3)]*3)
    for r in row:
        print(''.join(v[r+c].center(b)+('|' if c in '36' else '') for c in col))
        if r in 'CF': print(l)
    print
