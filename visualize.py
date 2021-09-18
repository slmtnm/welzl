from welzl import Circle, Welzl, Point
import plotly

with open('input.txt') as f:
    points = [Point(*line.split()) for line in f]

circle = Circle([points[i] for i in Welzl(points).sed()])