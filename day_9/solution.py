import copy

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


def part2(input_text):
  # list is column, row bc they be SNEAKY
  red_tile_coord_list = parse_input(input_text)
  red_tile_list = []
  largest_row_value = 0
  largest_col_value = 0

  for tile in red_tile_coord_list:
    tile_coords = tile.split(',')
    x = int(tile_coords[1])
    y = int(tile_coords[0])
    red_tile_list.append({
      'x': x,
      'y': y
    })
    if x > largest_row_value:
      largest_row_value = x
    if y > largest_col_value:
      largest_col_value = y

  # biggest row value + 1
  rows = largest_row_value + 2
  # biggest col value + 1
  cols = largest_col_value + 2

  # Create the 2D grid of dots
  grid = [["." for _ in range(cols)] for _ in range(rows)]

  # loop through list and set red and green tiles
  for i, coord1 in enumerate(red_tile_list):
    for j, coord2 in enumerate(red_tile_list):
      if i >= j:
        continue  # skip self and duplicates
      grid[coord1['x']][coord1['y']] = 'R'
      grid[coord2['x']][coord2['y']] = 'R'

      # fill in a straight line green tiles - we can assume AOC data is well formed for this
      # find which match - 
      if (coord1['x'] == coord2['x']):
        # x's match, fill between them
        if coord1['y'] > coord2['y']:
          # fill columns with coord1 larger
          for y in range(coord1['y'] - 1, coord2['y'], -1):
            grid[coord1['x']][y] = 'G'
        else:
          # fill columns with coord2 larger
          for y in range(coord2['y'] - 1, coord1['y'], -1):
            grid[coord1['x']][y] = 'G'

      elif (coord1['y'] == coord2['y']):
        # y's match fill between them
        if coord1['x'] > coord2['x']:
          # fill columns with coord1 larger
          for x in range(coord1['x'] - 1, coord2['x'], -1):
            grid[x][coord1['y']] = 'G'
        else:
          # fill columns with coord2 larger
          for x in range(coord2['x'] - 1, coord1['x'], -1):
            grid[x][coord1['y']] = 'G'
      else:
        # print(f"can't be straight line ignoring!: {coord1} and {coord2}")
        continue

  # go row by row, and fill all toggled items between r's and g's
  for i, row in enumerate(grid):
    # Find all boundary indices (red or green)
    boundary_indices = [j for j, cell in enumerate(row) if cell in ('R', 'G')]

    # Fill between each consecutive boundary pair
    for start, end in zip(boundary_indices, boundary_indices[1:]):
      for j in range(start + 1, end):
        if row[j] == '.':
          row[j] = 'G'


  print_map(grid)

  # ok find the area now!
  area_list = []

  # calculate area between all coords
  for i, coord1 in enumerate(red_tile_list):
    for j, coord2 in enumerate(red_tile_list):
      # Skip self and duplicate pairs
      if i >= j:
          continue
      
      # check if other corners are in the grid
      if (are_other_corners_in_grid):
        if (is_rectange_filled(grid, coord1, coord2)):
          # get the area between the pairs
          area_list.append((area_between_two_points(coord1, coord2), coord1, coord2))

  # find the largest area
  area_list.sort(key=lambda x: x[0], reverse=True)

  return area_list[0][0]


def area_between_two_points(tile1, tile2):
  width = abs(tile1['x'] - tile2['x']) + 1
  height = abs(tile1['y'] - tile2['y']) + 1
  distance = width * height
  # print(f"tile 1: {tile1}, tile 2: {tile2}, distance: {distance}")
  # print(f"{width} * {height}")
  return distance

def are_other_corners_in_grid(tile1, tile2):
  other_corner1 = (tile1['x'], tile2['y'])
  other_corner2 = (tile2['x'], tile1['y'])

  if (other_corner1 == 'R' or other_corner1 == 'G') and (other_corner2 == 'R' or other_corner2 == 'G'):
    return True
  return False

def is_rectange_filled(grid, coord1, coord2):
  x1, y1 = coord1['x'], coord1['y']
  x2, y2 = coord2['x'], coord2['y']

  # Sort coordinates
  x_start, x_end = sorted([x1, x2])
  y_start, y_end = sorted([y1, y2])

  # Check if rectangle is filled
  valid = True
  for x in range(x_start, x_end + 1):
    for y in range(y_start, y_end + 1):
      if grid[x][y] not in ('R', 'G'):
        valid = False
        break
    if not valid:
      break

  return valid
