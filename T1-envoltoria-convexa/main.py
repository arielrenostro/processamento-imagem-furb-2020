import collections
from typing import List
from convex import Point
from convex import graham_scan


class Gallery:
    points: List[Point]
    error: str

    def __init__(self):
        self.points = []
        self.error = ''


def read_gallery(lines) -> Gallery:
    gallery = Gallery()

    gallery_size = int(next(lines))
    if gallery_size < 3 or gallery_size > 50:
        gallery.error = 'Gallery size must be 3 <= SIZE <= 50'
        return gallery

    line_number = 0
    while line_number < gallery_size:
        x, y = list(
            map(lambda item: int(item), next(lines).split(' '))
        )

        if x < 0 or x > 1000 or y < 0 or y > 1000:
            gallery.error = f'Gallery point ({x}, {y}) is invalid. Must be 0 <= x,y <= 1000'
            gallery.points = []
            return gallery

        gallery.points.append(
            Point(x, y)
        )

        line_number += 1

    return gallery


def generate_galleries_by_iter(lines):
    galleries = []

    if not isinstance(lines, collections.Iterable):
        return galleries

    while True:
        try:
            gallery = read_gallery(lines)
            galleries.append(gallery)
        except StopIteration:
            break

    return galleries


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = iter(file.readlines())
    galleries = generate_galleries_by_iter(lines)

    for gallery in galleries:
        if gallery.error:
            print(gallery.error)
            continue

        convex_points = graham_scan(gallery.points)
        if all(point in convex_points for point in gallery.points):
            print('No')
        else:
            print('Yes')
