def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines() 
  return array_of_strings


def part1(input_text):
  # loop over data
  # detect if R or L
  # if L, and current - number becomes negative, take remainder and subtract from 99
  # if R, and current + number goes > 99, take the remainder and add to 0
  # keep track of num zero count and increment

  instructions = parse_input(input_text)

  count_zeroes = 0
  # dial starts pointing at 50
  current_number = 50
  for instruction in instructions:
    # parse the string
    direction = instruction[0]
    # number
    number_str = instruction[1:]
    if len(number_str) > 2:
      # just grab the last 2 numbers, in this case
      number_str = number_str[-2:]
      # print("greater than 2 numbers", instruction[1:], number_str)
    number = int(number_str)

    # print("instruction", instruction)
    # print("current number", current_number)
    # print("adjusted number", number)

    if direction == "R":
      added_together = current_number + number
      if added_together > 99:
        current_number = added_together - 100
      else:
        current_number = added_together
    else:
      subtracted_together = current_number - number
      if subtracted_together < 0:
        current_number = 100 + subtracted_together
      else:
        current_number = subtracted_together

    # print("after Number", current_number)
    if current_number == 0:
      count_zeroes += 1

  return count_zeroes


def part2(data):
    """Solve part 2 of the puzzle."""
    pass