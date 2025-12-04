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


# def part2(input_text):
#   bank_list = parse_input(input_text)
#   total_output_joltage = 0

#   for bank in bank_list:
#     running_string = ''
#     largest_number_index = 0
#     largest_number = 0
#     count_up = 0

#     for count in reversed(range(12)):
#       remaining_count = count + 1
#       largest_number, largest_number_index = loop_over_string(bank, remaining_count, count_up)
#       running_string = running_string + str(largest_number)
#       count_up = largest_number_index + count_up + 1
#     total_output_joltage += int(running_string)

#   return total_output_joltage


# def loop_over_string(bank, remaining_count, index_plus_count):
#   largest_number = 0
#   largest_number_index = 0
#   bank_substring = bank[index_plus_count:]

#   for index, jolt in enumerate(bank_substring):
#     jolt_num = int(jolt)
#     if jolt_num > largest_number and index <= len(bank_substring) - remaining_count:
#       largest_number = jolt_num
#       largest_number_index = index
#   return largest_number, largest_number_index