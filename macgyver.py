""" main file: allows the link between the different modules. """

import pygame
from pygame.locals import *
import constant
import stage
import player


def main():
    """ main loop manager """
    play = True
    pygame.init()
    screen = pygame.display.set_mode(constant.WINDOW)
    pygame.time.Clock().tick(30)
    pygame.key.set_repeat(500, 100)
    win = pygame.image.load("sprites/win.png").convert()
    lose = pygame.image.load("sprites/los.png").convert()

    while play:
        run = True
        items = stage.Items()
        mac = player.Character(stage.maze)
        stage.maze.display(screen, mac)
        items.drop_item(stage.maze)

        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        play = False
                        run = False
                    elif event.key == K_RIGHT:
                        mac.move("right")
                    elif event.key == K_LEFT:
                        mac.move("left")
                    elif event.key == K_UP:
                        mac.move("up")
                    elif event.key == K_DOWN:
                        mac.move("down")
                stage.maze.display(screen, mac)
                pygame.display.update()

            if stage.maze.laby[mac.tile_y][mac.tile_x] == "A":
                if constant.FIGHT_GUARDIAN is True:
                    screen.blit(win, (0, 0))
                    play = False
                    run = False
                elif constant.FIGHT_GUARDIAN is False:
                    screen.blit(lose, (0, 0))
                    items.drop_reset(stage.maze)
                    mac.inventory_reset()
                    run = False
                pygame.display.update()
                pygame.time.wait(1200)

if __name__ == "__main__":
    main()
