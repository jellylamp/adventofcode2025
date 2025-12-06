import copy

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
      split_list = line.split(' ')
      print(split_list)
      array2D.append(split_list)
  return array2D

# jesus christ gnome math
def part2(input_text):
  homework_map = parse_input_2d_part2(input_text)
  grand_total_sum = 0
  # transpose so we can loop through columns then rows
  transposed_homework_map = [list(row) for row in zip(*homework_map)]
  fixed_padding_map = fix_map_padding(transposed_homework_map)
  print_map(fixed_padding_map)

  print ("-----------------------------------------")
  for col_index, col_val in enumerate(fixed_padding_map):
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
      # now that our numbers match we can add / multiply them accordingly
      for char_index, character in enumerate(row_val):
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

def fix_map_padding(transposed_homework_map):
  # the original 2d parser filtered out empties so will have the correct cell counts
  fixed_map = copy.deepcopy(transposed_homework_map)

  # make this map have all empty cells
  for col_index, col_val in enumerate(transposed_homework_map):
    for row_index, row_val in enumerate(col_val):
      fixed_map[col_index][row_index] = ''


  for col_index, col_val in enumerate(transposed_homework_map):
    highest_val_char_count = 0

    # do a quick loop to determine max character count in row? aka 4 character num like 1000 determines what we add to
    for row_index, row_val in enumerate(col_val):
      char_count = len(row_val) - 1
      if char_count > highest_val_char_count:
        highest_val_char_count = char_count

    empty_character_count = 0
    # now loop over this with this knowledge in hand and fix padding
    for row_index, row_val in enumerate(col_val):
      # if character is a space, we know we need to add it to an item coming in the future
      if (row_val == ''):
        print(f"row val is empty, empty char count is {empty_character_count}")
        empty_character_count += 1
        continue

      value_char_count = len(row_val) - 1
      char_difference = highest_val_char_count - value_char_count
      print(f"value char count: {value_char_count}; char_difference: {char_difference}; row_value: {row_val}")
      
      if (char_difference != 0):
        # pad our number with trash to ignore so that the counts match
        if (empty_character_count > 0):
          # pad it to the front
          padded_number = '@' * char_difference + row_val
          empty_character_count = empty_character_count - char_difference
          print(f"char count isn't empty, padding the front: {padded_number}")
        else:
          # pad it to the back
          padded_number = row_val + '@' * char_difference
          print(f"char count empty, padding the back: {padded_number}")
        fixed_map[col_index][row_index] = padded_number
      else:
        fixed_map[col_index][row_index] = row_val

  # remove all remaining empty cells
  fixed_map_no_emptys = copy.deepcopy(fixed_map)
  for row_index, row in enumerate(fixed_map):
    fixed_row = list(filter(None, row))
    fixed_map_no_emptys[row_index] = fixed_row

  return fixed_map_no_emptys
      