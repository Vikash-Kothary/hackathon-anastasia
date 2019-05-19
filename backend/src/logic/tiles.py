#!/usr/bin/env python3
"""
tiles.py - Tiles
"""

class Tiles(object):

	def __init__(self, **kwargs):
		self.x_min = kwargs.get('x_min', 1980)
		self.x_max = kwargs.get('x_max', 2070)
		self.y_min = kwargs.get('y_min', 1320)
		self.y_max = kwargs.get('y_max', 1396)

# Initial Blank Tiles for the UK
def get_blank_tiles():
    k = 0
    all_tiles = dict()
    for i in range(y_min, y_max):
        for j in range(x_min, x_max):
            all_tiles[k] = dict()
            all_tiles[k]['location'] = (i, j)
            k+=1
    return all_tiles
all_tiles = get_blank_tiles()
#pprint_json(all_tiles)
#assert len(all_titles) is 6480

if __name__ == '__main__':
	pass