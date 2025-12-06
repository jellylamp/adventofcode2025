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

def parse_input_2d_part2(input_text):
  array2D = []
  with open(input_text, 'r') as f:
    for line in f.read().splitlines():
      split_list = line.split(' ')
      print(split_list)
      array2D.append(split_list)
  return array2D

# jesus christ gnome math
def part2(input_text):
  homework_map = parse_input_2d_part2(input_text)
  grand_total_sum = 0
  # transpose so we can loop through columns then rows
  transposed_homework_map = zip(*homework_map)
  print_map(homework_map)

  for col_index, col_val in enumerate(transposed_homework_map):
    # grab the last item so we know the operator
    operator = col_val[len(col_val) - 1]
    math_answer = 0
    highest_val_char_count = 0
    # numbers are max 4 digits looks like
    answer_array = [0, 0, 0, 0]

    # do a quick loop to determine max character count in row? aka 4 character num like 1000 determines what we add to
    for row_index, row_val in enumerate(col_val):
      char_count = len(row_val) - 1
      if char_count > highest_val_char_count:
        highest_val_char_count = char_count

    # now loop over this with this knowledge in hand
    for row_index, row_val in enumerate(col_val):
      value_char_count = len(row_val) - 1
      char_difference = highest_val_char_count - value_char_count
      # pad our number with trash to ignore so that the counts match
      padded_number = row_val + '@' * char_difference
      print("current value we are looping over", row_val)

      # now that our numbers match we can add / multiply them accordingly
      for char_index, character in enumerate(padded_number):
        if character == '@' or character == '*' or character == '+' or character == ' ':
          # skip this character
          continue
    
        print("answer array", answer_array)

        if row_index == 0:
          print(f"first index, answer array index {char_index} becomes {character}")
          answer_array[char_index] = int(character)
          continue

        math_answer = answer_array[char_index]
        if operator == '*':
          print(f"multiply {math_answer} with {character} = {math_answer * int(character)}")
          math_answer = math_answer * int(character)
        else:
          print(f"add  {math_answer} with {character} = {math_answer + int(character)}")
          math_answer = math_answer + int(character)
        answer_array[char_index] = math_answer

    total_sum = sum(answer_array)
    print(f"total sum = {total_sum}")
    grand_total_sum = grand_total_sum + total_sum
    print(f"grand total sum = {grand_total_sum}")
  
  return grand_total_sum
