import sys
from itertools import combinations
input = sys.stdin.readline

arr=[]
for _ in range(9):
    arr.append(int(input()))

for i in combinations(arr,7):
    if sum(i) == 100:
        for x in sorted(i):
            print(x)
        break