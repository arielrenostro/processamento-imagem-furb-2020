from typing import List


class Point:
    x: int = 0
    y: int = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'p({self.x},{self.y})'

    def __repr__(self):
        return f'p({self.x},{self.y})'


def last(stack):
    return stack[-1]


def penultimate(stack):
    return stack[-2]


def ccw(p1: Point, p2: Point, p3: Point) -> int:
    if p1 and p2 and p3:
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def graham_scan_partial(points):
    stack = []
    for point in points:
        while len(stack) > 1 and ccw(penultimate(stack), last(stack), point) < 0:
            stack.pop(-1)
        stack.append(point)
    stack.pop(-1)
    return stack


def graham_scan(points: List[Point]) -> List[Point]:
    if len(points) < 3:
        raise Exception('Needs 3 points to determine the convex')

    points.sort(key=lambda p: p.x)

    lower_stack = graham_scan_partial(points)
    upper_stack = graham_scan_partial(reversed(points))

    return [*lower_stack, *upper_stack]
