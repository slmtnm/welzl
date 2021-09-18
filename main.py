from welzl import Welzl, Point

with open('input.txt') as f:
    points = [Point(*line.split()) for line in f]

for index in Welzl(points).sed():
    print(index)