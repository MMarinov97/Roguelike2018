import libtcodpy as libtcod
from input_handler import handle_keys
from random import randint
from entity import Entity
from map_objects.cellular_map_generation import GameMap
from map_objects.game_map import GameMap as roomGameMap
from fov_functions import initialize_fov, recompute_fov
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

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 5

    # Dictionary to hold colors we'll be using
    colors =  {
        'dark_wall': libtcod.Color(48, 98, 48),
        'dark_ground': libtcod.Color(100, 140, 15),
        'light_wall': libtcod.Color(110, 110, 48),
        'light_ground': libtcod.Color(155, 188, 15),
        'unexplored': libtcod.Color(15, 56, 15)
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
    # We create a map randomly from the available options
    map_type = randint(0, 1)
    if map_type == 0:
        game_map = GameMap(map_width, map_height)
        game_map.make_map(65, map_width, map_height, player)
    else:
        room_num = randint(5, max_rooms)
        game_map = roomGameMap(map_width, map_height)
        game_map.make_map(room_num, room_min_size, room_max_size, map_width, map_height, player)
    # Fov doesn't need to be computed every turn, only if we move. We use
    # the boolean fov_recompute to handle this
    fov_recompute = True

    fov_map = initialize_fov(game_map)
    # Key for holding key presses and mouse variable
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Game Loop
    while not libtcod.console_is_window_closed():
        # Check for keypress
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        # Calculate fov
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)

        fov_recompute = False
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
                fov_recompute = True
        if exit:
            return True
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen()) # On and off
            
if __name__ == '__main__':
    main()