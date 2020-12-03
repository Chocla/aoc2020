from itertools import count, takewhile
from math import prod
with open('input.txt','r') as f:
    s = f.read().split('\n')

#### REASONABLE SOLUTION
# def part1(s,dx,dy):
#     count = 0
#     x = 0
#     y = 0
#     while y < len(s):
#         count += s[y][x%len(s[0])] == '#'
#         x += dx
#         y += dy
#     return count
# def part2(s):
#     deltas = [(1,1),(3,1),(5,1),(7,1),(1,2)]
#     ans = 1
#     for d in deltas:
#         ans *= part1(s,*d)
#     return ans


#### COOLER SOLUTION
print(sum(map(lambda p: s[p[1]][p[0]%len(s[0])] == '#', takewhile(lambda p: p[1] < len(s), zip(count(0,3),count(0,1))))))
print(prod(sum(map(lambda p: s[p[1]][p[0]%len(s[0])] == '#', takewhile(lambda p: p[1] < len(s), zip(count(0,d[0]),count(0,d[1]))))) for d in [(1,1),(3,1),(5,1),(7,1),(1,2)]))