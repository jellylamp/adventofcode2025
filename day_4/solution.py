import copy

def parse_input_2d(input_text):
  array2D = []
  with open(input_text, 'r') as f:
    for line in f.read().splitlines():
      array2D.append(list(line))
  return array2D

def print_map(grid):
  print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in grid]))

def checkNeighbors(grid, row, column):
  north = "."
  east = "."
  south = "."
  west = "."
  ne = "."
  nw = "." 
  se ="."
  sw = "."

  # North
  if row > 0:
    north = grid[row-1][column]

  # NE
  if row > 0 and column < len(grid) - 1:
    ne = grid[row - 1][column + 1]

  # East
  if column < len(grid) - 1:
    east = grid[row][column + 1]

  # SE
  if column < len(grid) - 1 and row < len(grid) - 1:
    se = grid[row + 1][column + 1]

  # South
  if row < len(grid) - 1:
    south = grid[row+1][column]

  # SW
  if row < len(grid) - 1 and column > 0:
    sw = grid[row+1][column - 1]

  # West
  if column > 0:
    west = grid[row][column - 1]

  # nw
  if column > 0 and row > 0:
    nw = grid[row-1][column-1]

  full_count = [north, east, south, west, ne, nw, se, sw].count("@")
  return full_count < 4


def part1(input_text):
  forklift_map = parse_input_2d(input_text)
  filled_out_map = copy.deepcopy(forklift_map);
  movable_count = 0

  for row_index, row_val in enumerate(forklift_map):
    for col_index, col_val in enumerate(row_val):
      # check if @; else continue
      if col_val == '.':
        continue

      # check neighbors for .
      if checkNeighbors(forklift_map, row_index, col_index):
        movable_count += 1
        filled_out_map[row_index][col_index] = "X"
  
  print_map(filled_out_map)
  return movable_count


def part2(input_text):
  forklift_map = parse_input_2d(input_text)
  filled_out_map = copy.deepcopy(forklift_map);
  movable_count_total = 0
  movable_count = 1

  while movable_count > 0:
    movable_count = 0
    for row_index, row_val in enumerate(forklift_map):
      for col_index, col_val in enumerate(row_val):
        # check if @; else continue
        if col_val != '@':
          continue

        # check neighbors for .
        if checkNeighbors(forklift_map, row_index, col_index):
          movable_count += 1
          filled_out_map[row_index][col_index] = "X"
    
    movable_count_total += movable_count
    forklift_map = copy.deepcopy(filled_out_map);


  return movable_count_total
