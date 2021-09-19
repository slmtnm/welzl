from __future__ import annotations
from typing import List
from random import shuffle

EPSILON = 1e-4

class Point:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __eq__(self, p: object) -> bool:
        return isinstance(p, Point) and self.x == p.x and self.y == p.y

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def __add__(self, p: Point) -> Point:
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, multiplier: float) -> Point:
        return Point(self.x * multiplier, self.y * multiplier)
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)
    
    def len2(self) -> float:
        return self.x**2 + self.y**2
    

class Circle:
    def __init__(self, P: List[Point]) -> None:
        '''Initialize new circle instance

        Input cases are:
        * If no points given (P is empty), then circle has invalid state.
        * If one point given, then circle has center at that point 
            and radius equals to 0.
        * If two points given, then circle has center at mean of those
            points and radius equals to half length of segment, connecting
            those two points.
        * If three points given, circle is circumscribed circle of triangle.
        * If more than three points given, ValueError exception is thrown.

        Arguments: P(List[Point]) - list of 0, 1, 2 or 3 points 
            that determine circle
        '''
        self.valid = bool(P)
        if not self.valid:
            return

        P = self._handle(P)
        if not P:
            self.center = Point(0, 0)
            self.radius2 = .0
        elif len(P) == 1:
            self.center = P[0]
            self.radius2 = .0
        elif len(P) == 2:
            self.center = (P[1] + P[0]) * .5
            self.radius2 = (P[1] - P[0]).len2() / 4
        else:
            p1, p2, p3 = P
            if abs(p1.x - p2.x) < EPSILON:
                p2, p3 = p3, p2
            elif abs(p2.x - p3.x) < EPSILON:
                p1, p2 = p2, p1
            ma = (p2.y - p1.y) / (p2.x - p1.x)
            mb = (p3.y - p2.y) / (p3.x - p2.x)
            
            # ma never equal to mb due to _handle function
            x = (ma*mb*(p1.y - p3.y) + mb*(p1.x + p2.x) - ma*(p2.x + p3.x)) / (2*(mb - ma))            
            if ma != 0:
                y = -1/ma*(x - (p1.x + p2.x) / 2) + (p1.y + p2.y)/2
            else:
                y = -1/mb*(x - (p2.x + p3.x) / 2) + (p2.y + p3.y)/2
            self.center = Point(x, y)
            self.radius2 = (self.center - p1).len2()
    
    def _handle(self, P: List[Point]) -> List[Point]:
        '''Sanitize input points by handling corner cases

        Corners cases are:
        * given 2 points that are equal; result will be one point
        * given 3 points, some of them are equal; result will be unique points
        * given 3 points that lie on same line; result will be 2 extreme points

        Arguments: P(List[Point]) - list of points that should be sanitized
        Returns: (List[Point]) - sanitized list of points
        '''
        if len(P) == 2 and P[0] == P[1]:
            # two points but they are the same
            return [P[0]]
        elif len(P) == 3:
            unique = list(set(P))
            if len(unique) < 3:
                # two or more points are the same
                return unique
            v = P[1] - P[0]
            n = Point(v.y, -v.x)
            c = -P[0].x*n.x - P[0].y*n.y
            if -EPSILON < P[2].x*n.x + P[2].y*n.y + c < EPSILON:
                # three points on same line
                if -EPSILON < n.x < EPSILON:
                    s = sorted(P, key=lambda p: p.x)
                else:
                    s = sorted(P, key=lambda p: p.y)                    
                return [s[0], s[2]]
        return P

    def contains(self, p: Point) -> bool:
        '''Checks whether circle contains point

        Arguments: p(Point) - point to check if it is in circle

        Returns: (bool) - true if circle contains point, false otherwise
        '''
        return self.valid and (self.center - p).len2() <= self.radius2

class Welzl:
    def __init__(self, points: List[Point]) -> None:
        self.points = points
        self.indices = list(range(len(points)))
        shuffle(self.indices)

    def sed(self) -> List[int]:
        '''Evaluates smallest enclosing disk

        Arguments: none

        Returns: (List[int]) - point indices in input point set, 
            given in constructor
        '''
        return self._welzl(P=self.indices, R=[])

    def _welzl(self, P: List[int], R: List[int]) -> List[int]:
        '''Recursive helper function

        Arguments: 
        * P(List[int]) - list of point indices that must be enclosed
        * R(List[int]) - list of point indices that must lie on enclosing circle

        Returns: (List[int]) - list of point indices, that determines minimal
            enclosing circle
        '''
        if not P or len(R) == 3:
            return R

        result = R
        for i, p in enumerate(P):
            if not Circle([self.points[i] for i in result]).contains(self.points[p]):
                result = self._welzl(P[:i], R + [p])
        return result