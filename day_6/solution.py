import copy

def parse_input_2d(input_text):
  array2D = []
  with open(input_text, 'r') as f:
    for line in f.read().splitlines():
      filtered_list = list(filter(None, line.split(' ')))
      array2D.append(filtered_list)
  return array2D

def print_map(grid):
  print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in grid]))

def part1(input_text):
  homework_map = parse_input_2d(input_text)
  grand_total_sum = 0
  # transpose so we can loop through columns then rows
  transposed_homework_map = zip(*homework_map)
  print_map(homework_map)

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

