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
    draw_hexagon(root, layout_hexagon((0, 0), hexagon_size), hexagon_size, "green")
    draw_hexagon(root, layout_hexagon((0, 2), hexagon_size), hexagon_size, "red")
    pygame.display.flip()
