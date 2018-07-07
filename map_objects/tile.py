class Tile:
    '''
    A tile on the map. It may be blocked and it may block sight
    '''
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        # By default if a tile is blocked you can't see through it
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
    