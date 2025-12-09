def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines()
  return array_of_strings

def print_map(grid):
  print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in grid]))

def part1(input_text):
  # list is column, row bc they be SNEAKY
  red_tile_coord_list = parse_input(input_text)
  red_tile_list = []

  for tile in red_tile_coord_list:
    tile_coords = tile.split(',')
    red_tile_list.append({
      'x': int(tile_coords[1]),
      'y': int(tile_coords[0])
    })

  area_list = []

  # calculate area between all coords
  for i, coord1 in enumerate(red_tile_list):
    for j, coord2 in enumerate(red_tile_list):
      # Skip self and duplicate pairs
      if i >= j:
          continue
      
      area_list.append((area_between_two_points(coord1, coord2), coord1, coord2))

  # find the largest area
  area_list.sort(key=lambda x: x[0], reverse=True)

  return area_list[0][0]


def area_between_two_points(tile1, tile2):
  width = abs(tile1['x'] - tile2['x']) + 1
  height = abs(tile1['y'] - tile2['y']) + 1
  distance = width * height
  print(f"tile 1: {tile1}, tile 2: {tile2}, distance: {distance}")
  print(f"{width} * {height}")
  return distance
  