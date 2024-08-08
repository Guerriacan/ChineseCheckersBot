from math import sin, cos, pi, sqrt
import pygame


def draw_hexagon(surface, center, size, color):
    x, y = center
    pygame.draw.polygon(surface, color, [
        (
            x + size * cos(pi / 180 * (60 * i - 30)),
            y + size * sin(pi / 180 * (60 * i - 30))
        )
        for i in range(6)
    ], 1)


def layout_hexagon(coord, size):
    q, r = coord
    x = w / 2 + size * sqrt(3) * (q + (r * -1) / 2)
    y = h / 2 - size * 3 / 2 * r
    return x, y


# coordinates for chinese checkers
BOARD = [
    (4, 8),
    (3, 7), (4, 7),
    (2, 6), (3, 6), (4, 6),
    (1, 5), (2, 5), (3, 5), (4, 5),
    (-4, 4), (-3, 4), (-2, 4), (-1, 4), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
    (-4, 3), (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
    (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
    (-4, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
    (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (-5, -1), (-4, -1), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), (3, -1), (4, -1),
    (-6, -2), (-5, -2), (-4, -2), (-3, -2), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), (3, -2), (4, -2),
    (-7, -3), (-6, -3), (-5, -3), (-4, -3), (-3, -3), (-2, -3), (-1, -3), (0, -3), (1, -3), (2, -3), (3, -3), (4, -3),
    (-8, -4), (-7, -4), (-6, -4), (-5, -4), (-4, -4), (-3, -4), (-2, -4), (-1, -4), (0, -4), (1, -4), (2, -4), (3, -4),
    (4, -4),
    (-4, -5), (-3, -5), (-2, -5), (-1, -5),
    (-4, -6), (-3, -6), (-2, -6),
    (-4, -7), (-3, -7),
    (-4, -8),
]

bg_color = (0, 0, 0)
fg_color = (0, 255, 255)
hexagon_size = 20

w, h = 1600, 900

pygame.init()
root = pygame.display.set_mode((w, h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    root.fill(bg_color)
    for coord in BOARD:
        draw_hexagon(root, layout_hexagon(coord, hexagon_size), hexagon_size, fg_color)
    draw_hexagon(root, layout_hexagon((4, 8), hexagon_size), hexagon_size, "green")
    draw_hexagon(root, layout_hexagon((-4, -8), hexagon_size), hexagon_size, "red")
    pygame.display.flip()
