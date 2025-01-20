#!.venv/bin/python3
import pygame
from speed import thread
import time
import random


def update_board(board):
    def callback(colum: list):
        colum = list(reversed(colum))
        for i, item in enumerate(colum):
            if colum[i-1] == None and item != (100, 100, 100):
                colum[i-1] = item
                colum[i] = None
        
        return list(reversed(colum))
    
    return thread(board, callback)

def add_tetromino(board):
    tetrominos = [
        ([(0, 0), (0, 1), (0, 2), (1, 1)], (0, 1))
    ]

    tetromino = random.choice(tetrominos)



window_size = (540, 960)
size = (12, 22)
sqere_size = (window_size[0] / size[0], window_size[1] / size[1])

board = [
    [(100, 100, 100) if y == size[1]-1 or x == 0 or x == size[0]-1 else None for y in range(size[1])] for x in range(size[0])
]

window = pygame.display.set_mode(window_size)

active_tetronimo = None

active = True
while active:
    print("tick")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not active_tetronimo:
                active_tetronimo = add_tetromino(board)
            continue
    
    window.fill((50, 75, 0))

    board = update_board(board)

    for x in range(size[0]):
        for y in range(size[1]):
            if not board[x][y]:
                continue

            pygame.draw.rect(
                window,
                board[x][y],
                pygame.Rect(x*sqere_size[0], y*sqere_size[1], sqere_size[0], sqere_size[1])
            )

    pygame.display.flip()

    time.sleep(1)