import random
import pygame
import sys
import os

position = (0, 0)

os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])


pygame.init()

screen = (400, 750)

window = pygame.display.set_mode(screen, pygame.SCALED)

pygame.display.set_caption("Piano Tiles")

clock = pygame.time.Clock()

white_tiles = []

black_tiles = []

speed = 40

Score = 0


class white_tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = True

    def draw(self, window):
        if self.status:
            self.rect = pygame.Rect(self.x, self.y, 100, 200)
            pygame.draw.rect(window, (255, 255, 255), self.rect)
        else:
            self.rect = pygame.Rect(self.x, self.y, 100, 200)
            pygame.draw.rect(window, (255, 0, 0), self.rect)


class black_tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = True

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, 100, 200)
        if self.status:
            pygame.draw.rect(window, (0, 0, 0), self.rect)
        else:
            pygame.draw.rect(window, (200, 200, 200), self.rect)


def move_tiles():
    for tile in white_tiles:
        tile.y += 3
    for tile in black_tiles:
        tile.y += 3


def draw_screen(window):
    window.fill(pygame.Color('green'))
    for tile in white_tiles:
        tile.draw(window)
    for tile in black_tiles:
        tile.draw(window)
    font = pygame.font.SysFont('Arial', 24)
    img = font.render(str(Score), True, pygame.Color('blue'))
    window.blit(img, (0, 0))
    pygame.display.update()


def new_line():
    global speed
    black_tile_location = random.randrange(0, 400, 100)
    speed += 2
    if len(white_tiles) != 0:
        for location in range(0, 400, 100):
            if location != black_tile_location:
                white_tiles.append(white_tile(location, black_tiles[-1].y - 200))
    else:
        for location in range(0, 400, 100):
            if location != black_tile_location:
                white_tiles.append(white_tile(location, 0))

    if len(black_tiles) != 0:
        black_tiles.append(black_tile(black_tile_location, black_tiles[-1].y - 200))
    else:
        black_tiles.append(black_tile(black_tile_location, 0))


def tile_check():
    global game_over
    for tile in black_tiles:
        if tile.y == 750 and tile.status == True:
            game_over = True
    if len(black_tiles) != 0:
        if black_tiles[-1].y > 0:
            new_line()
    else:
        new_line()
    for tile in white_tiles:
        if tile.y > 750:
            white_tiles.pop(white_tiles.index(tile))
    for tile in black_tiles:
        if tile.y > 750:
            black_tiles.pop(black_tiles.index(tile))


game_over = False

# main
while not game_over:
    clock.tick(speed)

    mouse_position = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    for tile in white_tiles:
        if tile.rect.collidepoint(mouse_position) and pressed1:
            tile.status = False
            tile.draw(window)
            pygame.time.delay(500)
            print(f"{Score} points!")
            game_over = True

    for tile in black_tiles:
        if tile.rect.collidepoint(mouse_position) and pressed1:
            if tile.status:
                Score += 1
            tile.status = False

    tile_check()
    draw_screen(window)
    move_tiles()

pygame.quit()
sys.exit()
