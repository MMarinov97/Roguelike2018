import libtcodpy as libtcod

def render_all(con, entities, game_map, screen_width, screen_height, colors):
    # Draws all the tiles in a map
    for y in range(game_map.height):
        for x in range(game_map.width):
            # We get if the tile with x and y coords is a wall and draw depending on what it is
            wall =  game_map.tiles[x][y].block_sight
            if wall:
                libtcod.console_set_default_foreground(con, libtcod.black)
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                libtcod.console_put_char(con, x, y, '#', libtcod.BKGND_NONE)
            else:
                libtcod.console_set_default_foreground(con, libtcod.black)
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
                libtcod.console_put_char(con, x, y, '.', libtcod.BKGND_NONE)
    # Draws all entities on top of the tiles
    for entity in entities:
        draw_entity(con, entity)
    
    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
def clear_all(con, entities):
    # Clears all entities in a list from a console
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    #  Clears the char that represents this entity
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)