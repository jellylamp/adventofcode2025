import re

def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines() 
  return array_of_strings


def part1(input_text):
  bank_list = parse_input(input_text)
  total_output_joltage = 0

  for bank in bank_list:
    largest_number = 0
    largest_number_index = 0
    second_largest_number = 0

    for index, jolt in enumerate(bank):
      jolt_num = int(jolt)
      if jolt_num > largest_number and index < len(bank) - 1:
        largest_number = jolt_num
        largest_number_index = index
       
    for index, jolt in enumerate(bank[largest_number_index + 1:]):
      jolt_num = int(jolt)
      if jolt_num > second_largest_number:
        second_largest_number = jolt_num

    concatted_jolt = str(largest_number) + str(second_largest_number)
    total_output_joltage += int(concatted_jolt)

  return total_output_joltage


def part2(input_text):
  bank_list = parse_input(input_text)
  total_output_joltage = 0

  for bank in bank_list:
    running_string = ''
    largest_number_index = 0
    largest_number = 0
    count_up = 0

    for count in reversed(range(12)):
      remaining_count = count + 1
      largest_number, largest_number_index = loop_over_string(bank, remaining_count, count_up)
      running_string = running_string + str(largest_number)
      count_up = largest_number_index + count_up + 1
    total_output_joltage += int(running_string)

  return total_output_joltage


def loop_over_string(bank, remaining_count, index_plus_count):
  largest_number = 0
  largest_number_index = 0
  bank_substring = bank[index_plus_count:]

  for index, jolt in enumerate(bank_substring):
    jolt_num = int(jolt)
    if jolt_num > largest_number and index <= len(bank_substring) - remaining_count:
      largest_number = jolt_num
      largest_number_index = index
  return largest_number, largest_number_index