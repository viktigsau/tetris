#!.venv/bin/python3
import pygame
from speed import thread
import time


def update_board(board):
    def callback(colum: list):
        for i, item in enumerate(colum.__reversed__()):
            if i != 0 and colum[-(i+1)] == None:
                colum[-(i+1)] = item
                colum[-i] = None
        
        return colum
    
    return thread(board, callback, use_threads=False)

window_size = (540, 960)
size = (12, 22)
sqere_size = (window_size[0]/size[0], window_size[1]/size[1])

board = [
    [(100, 100, 100) if y == size[1]-1 or x == 0 or x == size[0]-1 else None for y in range(size[1])] for x in range(size[0])
]
window = pygame.display.set_mode(window_size)

board[9][10] = (0, 255, 0)
board[9][9] = (255, 255, 0)
board[9][7] = (255, 0, 0)
board[9][1] = (0, 255, 255)
board[9][0] = (0, 0, 255)

active = True

while active:
    print("tick")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    
    window.fill((0, 0, 0))

    #board = update_board(board)

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