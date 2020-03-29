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


def ccw(p1: Point, p2: Point, p3: Point) -> int:
    if p1 and p2 and p3:
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def graham_scan(points: List[Point]) -> List[Point]:
    if len(points) < 3:
        raise Exception('Needs 3 points to determine the convex')

    points.sort(key=lambda p: p.x)

    lower_stack = []
    for point in points:
        while len(lower_stack) > 1 and ccw(lower_stack[-2], lower_stack[-1], point) < 0:
            lower_stack.pop(-1)
        lower_stack.append(point)

    upper_stack = []
    for point in reversed(points):
        while len(upper_stack) > 1 and ccw(upper_stack[-2], upper_stack[-1], point) < 0:
            upper_stack.pop(-1)
        upper_stack.append(point)

    lower_stack.pop(-1)
    upper_stack.pop(-1)

    return [*lower_stack, *upper_stack]
