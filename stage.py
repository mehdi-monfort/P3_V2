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
        syringue = pygame.image.load("sprites/syringue.jpg").convert()
        ether = pygame.image.load("sprites/ether.jpg").convert()
        tube = pygame.image.load("sprites/tube.jpg").convert()
        player = pygame.image.load("sprites/macgyver.png").convert_alpha()
        guardian = pygame.image.load("sprites/guardian.jpg").convert_alpha()
        hud = pygame.image.load("sprites/hud.jpg").convert()
        stars = pygame.image.load("sprites/stars.png").convert()

        for n_lin, line in enumerate(self.laby):
            for n_col, square in enumerate(line):
                square_x = n_lin * constant.SPRITE
                square_y = n_col * constant.SPRITE
                if square in ["+"]:
                    screen.blit(wall, (square_y, square_x))
                elif square in [" ", "S"]:
                    screen.blit(path, (square_y, square_x))
                elif square in ["A"]:
                    screen.blit(guardian, (square_y, square_x))
                elif square in ["e", "1"]:
                    screen.blit(ether, (square_y, square_x))
                elif square in ["s", "2"]:
                    screen.blit(syringue, (square_y, square_x))
                elif square in ["t", "3"]:
                    screen.blit(tube, (square_y, square_x))
                elif square in ["h", "u", "d", "/"]:
                    screen.blit(hud, (square_y, square_x))
                elif square in ["5"]:
                    screen.blit(stars, (square_y, square_x))
                if (n_lin, n_col) == (mac.tile_y, mac.tile_x):
                    screen.blit(player, (square_y, square_x))


maze = Level()


class Items:
    """ allows the management of objects in the maze """
    def __init__(self):
        self.maze = maze.laby
        self.items = ("e", "s", "t")
        self.item_x = self.item_y = " "
        self.place = []

    def drop_item(self, maze):
        """ drop item in the maze """
        for item in self.items:
            self.item_x, self.item_y = random.choice(maze.item)
            self.maze[self.item_y][self.item_x] = item
            self.place.append([self.item_y, self.item_x])

    def drop_reset(self, maze):
        print(self.place)
        for x, y in self.place:
            self.maze[x][y] = " "
