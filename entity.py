class Entity:
    '''
    A generic object to represent any player, enemy, item...
    '''
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
    
    def move(self, dx, dy):
        # Change the coordinates of the entity
        self.x += dx
        self.y += dy