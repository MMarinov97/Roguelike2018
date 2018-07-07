import libtcodpy as libtcod
# Key handler
def handle_keys(key):
    # Movement
    if(key.vk) == libtcod.KEY_DOWN:
        return {'move': (0, 1)} 
    if(key.vk) == libtcod.KEY_UP:
        return {'move': (0, -1)}
    if(key.vk) == libtcod.KEY_RIGHT:
        return {'move': (1 , 0)}
    if(key.vk) == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    # Other actions
    if(key.vk) == libtcod.KEY_ENTER and libtcod.KEY_ALT:
        return {'fullscreen': True}
    if(key.vk) == libtcod.KEY_ESCAPE:
        return {'exit': True}
    # No keypress...
    return {}
