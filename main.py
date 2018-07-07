import libtcodpy as libtcod
from input_handler import handle_keys
from random import randint
from entity import Entity
from map_objects.cellular_map_generation import GameMap
from render_functions import clear_all, render_all

def main():
    # Presets
    screen_width = 80
    screen_height = 50
    
    map_width = 80
    map_height = 45
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    # Dictionary to hold colors we'll be using
    colors =  {
        'dark_wall': libtcod.Color(15, 56, 15),
        'dark_ground': libtcod.Color(139, 172, 15)
    }
    # We declare an npc
    npc = Entity(int(screen_width/2 + 2), int(screen_height/2 - 5), '@', libtcod.grey)
    # We declare the player 
    player = Entity(int(screen_width/2), int(screen_height/2), '@', libtcod.white)
    # We get all entities in a list so we can iterate them
    entities = [player, npc]
    # Define the font and the screen...
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)


    libtcod.console_init_root(screen_width, screen_height, 'Roguelike',  False) # False because we dont want fullscreen
    # Main console
    con = libtcod.console_new(screen_width, screen_height)
    # Game map
    game_map = GameMap(map_width, map_height)
    roomNum = randint(5, max_rooms)
    game_map.make_map(65, map_width, map_height, player)
    # Key for holding key presses and mouse variable
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Game Loop
    while not libtcod.console_is_window_closed():
        # Check for keypress
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, screen_width, screen_height, colors)

        libtcod.console_flush()

        clear_all(con, entities)
        # We overwrite the character before getting the new coordinates, so next time we draw
        # it will not leave a trace
        '''
        Key handling
        We look for dictionary entries in action. If any of these is present it
        will be True.
        '''
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            # We check if we can actually move to the tile
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
        if exit:
            return True
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen()) # On and off
            
if __name__ == '__main__':
    main()