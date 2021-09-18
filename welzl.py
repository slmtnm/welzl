from __future__ import annotations
from typing import List
from random import shuffle

class Point:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def __add__(self, p: Point) -> Point:
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, multiplier: float) -> Point:
        return Point(self.x * multiplier, self.y * multiplier)
    
    def len2(self) -> float:
        return self.x**2 + self.y**2
    

class Circle:
    def __init__(self, P: List[Point]) -> None:
        if not P:
            self.center = Point(0, 0)
            self.radius2 = .0
        elif len(P) == 1:
            self.center = P[0]
            self.radius2 = .0
        elif len(P) == 2:
            self.center = (P[1] + P[0]) * .5
            self.radius2 = (P[1] - P[0]).len2()
        else:
            p1, p2, p3 = P
            # TODO: check if p1, p2, p3 lies on one line
            ma = (p2.y - p1.y) / (p2.x - p1.x)
            mb = (p3.y - p2.y) / (p3.x - p2.x)
            x = ma*mb*(p1.y - p3.y) + mb*(p1.x + p2.x) - ma*(p2.x + p3.x) / 2*(mb - ma)
            y = -1/ma*(x - (p1.x + p2.x) / 2) + (p1.y + p2.y)/2
            self.center = Point(x, y)
            self.radius2 = (self.center - p1).len2()

    def contains(self, p: Point) -> bool:
        return (self.center - p).len2() <= self.radius2


class Welzl:
    def __init__(self, points: List[Point]) -> None:
        self.points = points
        self.indices = list(range(len(points)))
        shuffle(self.indices)

    def sed(self) -> List[int]:
        return self._welzl(P=self.indices, R=[])

    def _welzl(self, P: List[int], R: List[int]) -> List[int]:
        if not P or len(R) == 3: 
            return R
        p, *rest = P
        D = self._welzl(rest, R)
        
        if Circle([self.points[i] for i in D]).contains(self.points[p]):
            return D
        
        return self._welzl(rest, R + [p])