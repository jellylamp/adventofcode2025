import copy
import math
from itertools import zip_longest

def parse_input_2d(input_text):
  array2D = []
  with open(input_text, 'r') as f:
    for line in f.read().splitlines():
      filtered_list = list(filter(None, line.split(' ')))
      array2D.append(filtered_list)
  return array2D

def print_map(grid):
  print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in grid]))

def part1(input_text):
  homework_map = parse_input_2d(input_text)
  grand_total_sum = 0
  # transpose so we can loop through columns then rows
  transposed_homework_map = zip(*homework_map)

  for col_index, col_val in enumerate(transposed_homework_map):
    # grab the last item so we know the operator
    operator = col_val[len(col_val) - 1]
    math_answer = 0

    for row_index, row_val in enumerate(col_val):
      if row_index == 0:
        math_answer = int(row_val)
        continue

      if row_index == len(col_val) - 1:
        continue

      if operator == '*':
        math_answer = math_answer * int(row_val)

      else:
        math_answer = math_answer + int(row_val)

    grand_total_sum = grand_total_sum + math_answer
  
  return grand_total_sum

def parse_input_2d_part2(input_text):
  array2D = []
  with open(input_text, 'r') as f:
    for line in f.read().splitlines():
      array2D.append(line)
  return array2D

# jesus christ gnome math
def part2(input_text, row_count):
  homework_map = parse_input_2d_part2(input_text)
  grand_total_sum = 0
  # transpose so we can loop through columns then rows
  transposed_homework_map = [list(col) for col in zip_longest(*homework_map, fillvalue=" ")]
  # print_map(transposed_homework_map)

  all_zero_column_indexes = []
  operations_order = []

  # do a quick loop and find the index of when all rows/columns have zeros.
  for col_idx, col in enumerate(transposed_homework_map):
    empty_space_count = 0
    for row in col:
      if row == ' ':
        empty_space_count += 1
        if empty_space_count == row_count + 1:
          # we found a boundary! put the column index in the list
          all_zero_column_indexes.append(col_idx)
      if row == '*' or row == '+':
        operations_order.append(row)

  # add the last column + 1to all zero row indexes
  all_zero_column_indexes.append(len(transposed_homework_map))
  # print(all_zero_column_indexes)

  # loop through for real
  number_boundary = all_zero_column_indexes.pop(0)
  running_numbers_array = []
  operator = operations_order.pop(0)

  for col_idx, col in enumerate(transposed_homework_map):
    running_number = ''
    if col_idx == number_boundary and col_idx != len(transposed_homework_map):
      running_numbers_array, grand_total_sum, number_boundary, operator = reset_and_sum(running_numbers_array, operator, grand_total_sum, all_zero_column_indexes, operations_order, False)
      continue

    for row_idx, row in enumerate(col):
      # don't care about operations row
      if row_idx == row_count:
        # this is the last row, add to the running number and move on
        running_numbers_array.append(running_number)
        continue
      
      # add to running number
      # print(row)
      running_number = running_number + row

  # add one last time
  running_numbers_array, grand_total_sum, number_boundary, operator = reset_and_sum(running_numbers_array, operator, grand_total_sum, all_zero_column_indexes, operations_order, True)

  return grand_total_sum

def reset_and_sum(running_numbers_array, operator, grand_total_sum, all_zero_column_indexes, operations_order, dont_pop):
  # print(running_numbers_array)
  int_running_numbers_array = [int(numeric_string.replace(" ", "")) for numeric_string in running_numbers_array]
  # do the math!
  if operator == '+':
    total = sum(int_running_numbers_array)
  else:
    total = math.prod(int_running_numbers_array)
  grand_total_sum += total
  print("running numbers array", int_running_numbers_array)
  print(f"operator: {operator}; total: {total}")

  # reset!
  # print(f"reset! all_zero_column_indexes before pop {all_zero_column_indexes}; all operators before pop {operations_order}")
  number_boundary = 0
  if dont_pop == False:
    number_boundary = all_zero_column_indexes.pop(0)
    operator = operations_order.pop()
    running_numbers_array = []
  return running_numbers_array, grand_total_sum, number_boundary, operator