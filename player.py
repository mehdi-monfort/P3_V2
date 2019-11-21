""" module player: used to manage the movement and the player's inventory. """
import constant
import stage


class Character:
    """ character management """

    def __init__(self, mac):
        self.it_inventory = []
        self.tile_x = mac.startx
        self.tile_y = mac.starty
        self.counter = 0
        self.it1 = self.it2 = self.it3 = stage.maze.laby

    def get_object(self, tile_x, tile_y):
        """ add an object to the inventory """
        if stage.maze.laby[tile_y][tile_x] in ["e", "s", "t"]:
            self.it_inventory.append(stage.maze.laby[tile_y][tile_x])
            stage.maze.laby[tile_y][tile_x] = " "
            self.counter += 1
        if "e" in self.it_inventory:
            self.it1[15][6] = "1"
        if "s" in self.it_inventory:
            self.it2[15][7] = "2"
        if "t" in self.it_inventory:
            self.it3[15][8] = "3"
        if self.counter == 3:
            constant.FIGHT_GUARDIAN = True
            self.it1[15][6] = self.it2[15][7] = self.it3[15][8] = "5"

    def inventory_reset(self):
        """ allows the inventory reset """
        self.counter = 0
        self.it1[15][6] = self.it2[15][7] = self.it3[15][8] = "/"

    def move(self, direction):
        """ move the character into the maze """
        if direction == "right":
            if self.tile_x < constant.N_SPRITE - 1:
                if stage.maze.laby[self.tile_y][self.tile_x + 1] != "+":
                    self.tile_x += 1
                    self.get_object(self.tile_x, self.tile_y)

        elif direction == "left":
            if self.tile_x > 0:
                if stage.maze.laby[self.tile_y][self.tile_x - 1] != "+":
                    self.tile_x -= 1
                    self.get_object(self.tile_x, self.tile_y)

        elif direction == "up":
            if self.tile_y > 0:
                if stage.maze.laby[self.tile_y - 1][self.tile_x] != "+":
                    self.tile_y -= 1
                    self.get_object(self.tile_x, self.tile_y)

        elif direction == "down":
            if self.tile_y < constant.N_SPRITE - 1:
                if stage.maze.laby[self.tile_y + 1][self.tile_x] != "+":
                    self.tile_y += 1
                    self.get_object(self.tile_x, self.tile_y)
