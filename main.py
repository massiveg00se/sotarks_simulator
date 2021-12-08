import pygame
import os
import random
from constants import *
import load_assets

# setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CURSOR_RECT = load_assets.CURSOR.get_rect()
pygame.display.set_caption('sotarks simulator')
pygame.mouse.set_visible(False)
game_status = False
font_48 = pygame.font.Font(os.path.join('assets', 'FiraCode-Regular.ttf'), 48)
welcome_text = font_48.render("Press any key to start", True, WHITE)

def main():
    global game_status
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not game_status:
                    game_status = True

        if game_status:
            game()
        else:
            start_screen()

    pygame.quit()

def start_screen():
    WIN.fill(BLACK)
    WIN.blit(welcome_text, (0, 0))
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def game():
    WIN.fill(BLACK)
    # stuff
    # end stuff
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def end_screen():
    WIN.fill(BLACK)
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def new_points(n):

    points = [(random.randint(150, 1130), random.randint(150, 570))]

    for i in range(n - 1):
        temp = True
        while temp:
            point = (random.randint(150, 1130), random.randint(150, 570))
            dist = ((point[0] - points[-1][0])**2 + (point[1] - points[-1][1])**2)**0.5
            if dist > 532:
                points.append(point)
                temp = False

    return points

def new_map(n):
    return [HitObject(i[0], i[1]) for i in new_points(n)]

'''
Generate n number of random points
Each point is at least 532 pixels from the previous point
points -> list of tuples in (x, y) format
screen margin of 150 pixels on all sides
allowed x [150, 1130]
allowed y [150, 570]
'''

def update_objects(objects, timing_point):
    pass

class HitObject: # circle size 128x128
    field = False # is the object on field?
    hit_window = False # is the hit window for the object active?
    field_time = 0  # time object has been on field in ms
    opacity = field_time / 400 if field_time <= 400 else 1  # opacity of object
    approach_mult = 2 - field_time / 400  # size of approach circle

    def __init__(self, x, y, timing_point):
        self.x = x
        self.y = y
        self.timing_point = timing_point

    def counter(self):
        self.field_time += 10


if __name__ == "__main__":
    main()
