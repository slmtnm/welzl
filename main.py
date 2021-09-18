from welzl import Welzl, Point
from sys import setrecursionlimit

with open('input.txt') as f:
    points = [Point(*line.split()) for line in f]

if len(points) > 2000:
    setrecursionlimit(len(points) + 2)

for index in Welzl(points).sed():
    print(index)