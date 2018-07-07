from random import randint
from map_objects.rectangle import Rect
from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def map_to_matrix(self):
        # Returns a 2D matrix, which is the dead/alive interpretation of the
        # current map. Uses False for dead, True for alive
        matrix = [[True for x in range(self.height)] for y in range(self.width)]
        for i in range(0, self.width):
            for j in range(0, self.height):
                matrix[i][j] = self.tiles[i][j].blocked 
        return matrix 

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
    def make_map(self, chance, map_width, map_height, player):
        # Initial setup of the matrix
        birthLimit = 4
        deathLimit = 3 
        matrix = self.map_to_matrix()
        for x in range(0, self.width):
            for y in range(0, self.height):
                if randint(0, 100) < chance:
                    matrix[x][y] = True

        # Now we iterate through the same rules to shape the cave
        for i in range(0, self.width-1):
            matrix[i][int(self.height/2)] = False
        for j in range(0, self.height):
            matrix[int(self.width/2)][j] = False

        for generation in range(0, 3):
            for i in range(1, self.width -1):
                for j in range(1, self.height -1):
                    aliveNum = self.count_alive_neighbours(i, j, matrix)
                    if matrix[i][j]:
                        # Cell is True -> Wall
                        if aliveNum > deathLimit:
                            self.tiles[i][j].blocked = False
                            self.tiles[i][j].block_sight = False
                        else:
                            self.tiles[i][j].blocked = True
                            self.tiles[i][j].block_sight = True
                    else:
                        # Cell is False -> Floor
                        if aliveNum < birthLimit:
                            self.tiles[i][j].blocked = True
                            self.tiles[i][j].block_sight = True
                        else:
                            self.tiles[i][j].blocked = False
                            self.tiles[i][j].block_sight = False
            # Now we copy the map on the matrix for the next gen
            matrix = self.map_to_matrix()

    def count_alive_neighbours(self, x, y, matrix):
        # We check all neighbours to see if they are alive
        aliveNum = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour_x = x + i
                neighbour_y = y + j
                if matrix[neighbour_x][neighbour_y] == False:
                    if j == 0 and i == 0:
                        aliveNum = aliveNum
                    else:
                        aliveNum += 1
                elif neighbour_x < 0 or neighbour_x > self.width or neighbour_y < 0 or neighbour_y > self.height:
                    aliveNum += 1
        return aliveNum


    def matrix_to_map(self, matrix):
        # Sets the mats tiles to wall or floor using the matrix as reference
        for i in range(0, self.width):
            for j in range(0, self.height):
                self.tiles[i][j].blocked = matrix[i][j]
                self.tiles[i][j].block_sight = matrix[i][j]