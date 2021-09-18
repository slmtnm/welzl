from math import sqrt

import plotly.graph_objects as go

from welzl import Circle, Point, Welzl
from random import randint
import sys

POINTS_NUMBER = 10_000

sys.setrecursionlimit(2 * POINTS_NUMBER)

points = [Point(randint(0, 100), randint(0, 100)) for _ in range(POINTS_NUMBER)]

indices = Welzl(points).sed()
result_points = [points[i] for i in indices]
circle = Circle(result_points)
r = sqrt(circle.radius2)

fig = go.Figure()
fig.update_xaxes(range=[-30, 130])
fig.update_yaxes(range=[-30, 130])
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=circle.center.x - r, y0=circle.center.y - r,
    x1=circle.center.x + r, y1=circle.center.y + r,
    line_color="LightSeaGreen",
)
xs, ys = [p.x for p in points], [p.y for p in points]
result_xs, result_ys = [p.x for p in result_points], [p.y for p in result_points]
fig.add_scatter(x=xs, y=ys, mode='markers', marker={'color': 'blue'})
fig.add_scatter(x=result_xs, y=result_ys, mode='markers', marker={'color': 'red'})
fig.update_layout(width=800, height=800)
fig.show()
