import re
from collections import defaultdict
s = open('input.txt','r').read().split('\n\n')
pattern = r"Tile (\d+):\n" #((\.|\#){10}\n){10}"
tiles = []
def getEdges(t):
    return t[0],t[-1],[x[0] for x in t], [x[-1] for x in t]
for l in s:
    tileID = int(re.match(pattern,l).groups(0)[0])
    tileGrid = []
    for row in l.split('\n')[1:]:
        tmp = []
        for col in row:
            tmp.append(int(col=='#'))
        tileGrid.append(tmp)

    tiles.append((tileID,tileGrid))

edgeCounts = defaultdict(int)
edgeToID = defaultdict(list)
for t in tiles:
    for edge in getEdges(t[1]):
        edgeCounts[(tuple(edge))] += 1
        edgeCounts[(tuple(reversed(edge)))] += 1
ans = 1
for t in tiles:
    c = 0
    for edge in getEdges(t[1]):
        if edgeCounts[(tuple(edge))] == 1 or edgeCounts[(tuple(reversed(edge)))] == 1:
            c += 1
    if c == 2:
        ans *= t[0]
print(ans)
