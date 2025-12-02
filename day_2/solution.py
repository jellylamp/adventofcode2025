import re

def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines() 
  return array_of_strings


def part1(input_text):
  id_list = parse_input(input_text)[0].split(',')

  invalid_id_sum = 0

  for id_range in id_list:
    range_start, range_end = id_range.split('-')

    range_start = int(range_start)
    range_end = int(range_end)

    # loop through the range numbers
    for num_to_check in range(range_start, range_end + 1):
      num_to_check_string = str(num_to_check)

      # if odd number of characters, continue
      if len(num_to_check_string)%2 != 0:
        continue

      # split the string in half
      half_1 = num_to_check_string[:len(num_to_check_string)//2]
      half_2 = num_to_check_string[len(num_to_check_string)//2:]

      if half_1 == half_2:
        print("invalid id", num_to_check)
        invalid_id_sum += int(num_to_check)

  return invalid_id_sum


def part2(input_text):
  id_list = parse_input(input_text)[0].split(',')

  invalid_id_sum = 0

  for id_range in id_list:
    range_start, range_end = id_range.split('-')

    range_start = int(range_start)
    range_end = int(range_end)

    # loop through the range numbers
    for num_to_check in range(range_start, range_end + 1):
      num_to_check_string = str(num_to_check)
      if check_string_factors(num_to_check_string):
        invalid_id_sum += num_to_check

  return invalid_id_sum

def check_string_factors(num_to_check_string):
  # max length string is 10, if we check all of these divisions then we have it.
  factors = [2, 3, 4, 5, 6, 7, 8, 9]

  # split the string by factor
  for factor in factors:
    # Check if string length can be split evenly by this factor
    if len(num_to_check_string)%factor != 0:
      continue

    split_evenly = re.findall('.{%d}' % (len(num_to_check_string) / factor), num_to_check_string)
    all_are_even = len(set(split_evenly)) == 1

    if all_are_even and split_evenly[0] != "":
      print("invalid id", num_to_check_string)
      return True
  return False