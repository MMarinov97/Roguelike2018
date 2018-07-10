import libtcodpy as libtcod
from random import randint
from map_objects.cellular_map_generation import GameMap
from map_objects.game_map import GameMap as roomGameMap
from entity import Entity
def render_map(con, game_map, screen_width, screen_height, colors):
	for x in range(0, screen_width):
		for y in range(0, screen_height):
			wall = game_map.tiles[x][y].blocked
			if wall:
				libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
				libtcod.console_set_default_foreground(con, libtcod.black)
				libtcod.console_put_char(con, x, y, '#', libtcod.BKGND_NONE)
			else:
				libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
				libtcod.console_set_default_foreground(con, libtcod.black)
				libtcod.console_put_char(con, x, y, '.', libtcod.BKGND_NONE)


def main():
	# Presets
	libtcod.sys_set_fps(60)
	screen_width = 80
	screen_height = 50
	map_width = screen_width
	map_height = screen_height

	max_rooms = 50
	room_max_size = 10
	room_min_size = 6
	max_monsters = 10

	colors = {
        'dark_wall': libtcod.Color(48, 98, 48),
        'dark_ground': libtcod.Color(100, 140, 15),
        'light_wall': libtcod.Color(110, 110, 48),
        'light_ground': libtcod.Color(155, 188, 15),
        'unexplored': libtcod.Color(15, 56, 15)
	}

	key = libtcod.Key()
	mouse = libtcod.Mouse()

	libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.console_init_root(screen_width, screen_height, 'Roguelike',  False) # False because we dont want fullscreen
	# Test
	player = Entity(int(screen_width/2), int(screen_height/2), '@', libtcod.white)
	entities = [player]

	con = libtcod.console_new(screen_width, screen_height)
	map_type = randint(0, 1)
	if map_type == 0:
		game_map = GameMap(map_width, map_height)
		game_map.make_map(80, map_width, map_height, player, max_monsters, entities)
	else:
		room_num = randint(10, max_rooms)
		game_map = roomGameMap(map_width, map_height)
		game_map.make_map(room_num, room_min_size, room_max_size, map_width, map_height, player, entities, 3)
	while not libtcod.console_is_window_closed():
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
		render_map(con, game_map, screen_width, screen_height, colors)
		render_map
		libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
		libtcod.console_flush()

if __name__ == '__main__':
	main()