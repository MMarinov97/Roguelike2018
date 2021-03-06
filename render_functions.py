import libtcodpy as libtcod

def render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors, player):
    # Draws all the tiles in a map
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall =  game_map.tiles[x][y].block_sight
                if visible:
                    if wall:
                        libtcod.console_set_default_foreground(con, libtcod.black)
                        libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, '#', libtcod.BKGND_NONE)
                    else:
                        libtcod.console_set_default_foreground(con, libtcod.black)
                        libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, '.', libtcod.BKGND_NONE)
                    game_map.tiles[x][y].explored = True
                else:
                    if game_map.tiles[x][y].explored:
                        if wall:
                            libtcod.console_set_default_foreground(con, libtcod.black)
                            libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                            libtcod.console_put_char(con, x, y, 178, libtcod.BKGND_NONE)
                        else:
                            libtcod.console_set_default_foreground(con, libtcod.black)
                            libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
                            libtcod.console_put_char(con, x, y, 176, libtcod.BKGND_NONE)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('unexplored'), libtcod.BKGND_SET)

    # Draws all entities on top of the tiles
    for entity in entities:
        draw_entity(con, entity, fov_map, colors)
    draw_UI(con, player, screen_width, screen_height)
    
    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
def clear_all(con, entities):
    # Clears all entities in a list from a console
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity, fov_map, colors):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)
def draw_UI(con, player, screen_width, screen_height):
    for x in range(0, screen_width):
        libtcod.console_set_char_background(con, x, 45, libtcod.dark_gray)
        for y in range(46, 50):
            libtcod.console_set_char_background(con, x, y, libtcod.grey)





def clear_entity(con, entity):
    #  Clears the char that represents this entity
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)