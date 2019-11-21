""" module level: used to create the labyrinth from the file "laby.txt". """
import pygame
import random
import constant


class Level:
    """ creation of the maze """
    def __init__(self):
        self.startx = 0
        self.starty = 0
        self.laby = []
        self.item = []

        with open("laby.txt", "r") as filename:
            for line in filename:
                maze_line = []
                for char in line:
                    if char != "\n":
                        maze_line.append(char)
                self.laby.append(maze_line)
            for n_lin, line in enumerate(self.laby):
                for n_col, square in enumerate(line):
                    if square in "S":
                        self.startx = n_col
                        self.starty = n_lin
                    if square in " ":
                        self.item.append([n_col, n_lin])

    def display(self, screen, mac):
        """ allows the display of sprites """
        wall = pygame.image.load("sprites/wall.jpg").convert()
        path = pygame.image.load("sprites/ground.jpg").convert()
<<<<<<< HEAD
        syringue = pygame.image.load("sprites/syringue.jpg").convert()
        ether = pygame.image.load("sprites/ether.jpg").convert()
        tube = pygame.image.load("sprites/tube.jpg").convert()
=======
        propeller = pygame.image.load("sprites/propeller.png").convert()
        magnet = pygame.image.load("sprites/magnet.png").convert()
        battery = pygame.image.load("sprites/battery.png").convert()
>>>>>>> 17dc858d9aa9ea1bef39ad2d8d301bfc1a41e1be
        player = pygame.image.load("sprites/macgyver.png").convert_alpha()
        guardian = pygame.image.load("sprites/guardian.jpg").convert_alpha()
        hud = pygame.image.load("sprites/hud.jpg").convert()
        stars = pygame.image.load("sprites/stars.png").convert()

        for n_lin, line in enumerate(self.laby):
            for n_col, square in enumerate(line):
                square_x = n_lin * constant.SPRITE
                square_y = n_col * constant.SPRITE
                if square in "+":
                    screen.blit(wall, (square_y, square_x))
                elif square in [" ", "S"]:
                    screen.blit(path, (square_y, square_x))
                elif square in "A":
                    screen.blit(guardian, (square_y, square_x))
                elif square in ["e", "1"]:
                    screen.blit(ether, (square_y, square_x))
                elif square in ["s", "2"]:
                    screen.blit(syringue, (square_y, square_x))
                elif square in ["t", "3"]:
                    screen.blit(tube, (square_y, square_x))
                elif square in ["h", "u", "d", "/"]:
                    screen.blit(hud, (square_y, square_x))
                elif square in "5":
                    screen.blit(stars, (square_y, square_x))
                if (n_lin, n_col) == (mac.tile_y, mac.tile_x):
                    screen.blit(player, (square_y, square_x))


maze = Level()


class Items:
    """ allows the management of objects in the maze """
    def __init__(self):
        self.laby = maze.laby
        self.ether_x = self.ether_y = 0
        self.tube_x = self.tube_y = 0
        self.syringue_x = self.syringue_y = 0

    def drop_ether(self, maze):
        """ drop the ether in the maze """
        ether = "e"
        self.ether_x, self.ether_y = random.choice(maze.item)
        self.laby[self.ether_y][self.ether_x] = ether

    def drop_tube(self, maze):
        """ drop the tube in the maze """
        tube = "t"
        self.tube_x, self.tube_y = random.choice(maze.item)
        self.laby[self.tube_y][self.tube_x] = tube

    def drop_syringue(self, maze):
        """ drop the syringue in the maze """
        syringue = "s"
        self.syringue_x, self.syringue_y = random.choice(maze.item)
        self.laby[self.syringue_y][self.syringue_x] = syringue

    def drop_reset(self, maze):
        self.laby[self.ether_y][self.ether_x] = " "
        self.laby[self.tube_y][self.tube_x] = " "
        self.laby[self.syringue_y][self.syringue_x] = " "
