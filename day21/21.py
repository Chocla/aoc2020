from collections import defaultdict
foodList = open('input.txt','r').read().split('\n')
candidates = defaultdict(set)

foods = []
allmap = defaultdict(set)
ingmap = defaultdict(set)

for i,food in enumerate(foodList):
    ingredients,allergies = food.split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergies = allergies[:-1].split(', ')
    for ing in ingredients:
        ingmap[ing].add(i)
    for _all in allergies:
        allmap[_all].add(i)

c = 0
safe = set()
for ing in ingmap:
    flag = True
    for _all in allmap:
        if allmap[_all].issubset(ingmap[ing]):
            flag = False
            break
    if flag:
        c += len(ingmap[ing])
        safe.add(ing)
for s in safe:
    ingmap.pop(s)
pairs = []
matrix = []
a = list(sorted(ingmap.keys()))
b = list(sorted(allmap.keys()))
for i in range(len(a)):
    tmp2 = []
    for j in range(len(b)):
        tmp2.append(int(ingmap[a[i]].issuperset( allmap[b[j]])))
    matrix.append(tmp2)
while (sum([sum(x) for x in matrix]) > 0):
    for i,row in enumerate(matrix):
        if sum(row) == 1:
            col = row.index(1)
            pairs.append((a[i],b[col]))
            for j in range(len(matrix)):
                matrix[j][col] = 0
print("".join([x[0] +',' for x in sorted(pairs,key = lambda x: x[1])])[:-1])
print(c)