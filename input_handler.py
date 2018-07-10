import libtcodpy as libtcod
# Key handler
def handle_keys(key):
    # Movement
    keyChar = chr(key.c)
    if keyChar == 'j':
        # DOWN
        return {'move': (0, 1)} 
    if keyChar == 'k':
        # UP
        return {'move': (0, -1)}
    if keyChar == 'l':
        # RIGHT
        return {'move': (1 , 0)}
    if keyChar == 'h':
        # LEFT
        return {'move': (-1, 0)}
    if keyChar == 'u':
        # UP + LEFT
        return {'move': (-1, -1)}
    if keyChar == 'i':
        # UP + RIGHT
        return {'move': (1 , -1)}
    if keyChar == 'n':
        # DOWN + LEFT
        return {'move': (-1, 1)}
    if keyChar == 'm':
        # DOWN + RIGHT
        return {'move': (1, 1)}
    # Other actions
    if(key.vk) == libtcod.KEY_ENTER and libtcod.KEY_ALT:
        return {'fullscreen': True}
    if(key.vk) == libtcod.KEY_ESCAPE:
        return {'exit': True}
    # No keypress...
    return {}
