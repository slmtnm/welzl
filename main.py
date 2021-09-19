from welzl import Welzl, Point
from sys import argv

if len(argv) < 2:
    print('Usage: python3 ./main.py <file-with-points>')
    exit(1)

with open(argv[1]) as f:
    points = [Point(*line.split()) for line in f]

for index in Welzl(points).sed():
    print(index)
