def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines() 
  
  # split on newline
  array_split_index = 0
  for index, line in enumerate(array_of_strings):
     if line == '' or line == '/n':
        array_split_index = index
        break
        
  fresh_ingredients = array_of_strings[0:array_split_index]
  test_ingredients = array_of_strings[array_split_index + 1:]
  return fresh_ingredients, test_ingredients


def part1(input_text):
  fresh_ingredients, test_ingredients = parse_input(input_text)
  fresh_range_arr = []
  fresh_count = 0
  
  # make a range dictionary
  for ingredient_range in fresh_ingredients:
     # parse out -
    ingredient_range_arr = ingredient_range.split('-')
    starting_range = ingredient_range_arr[0]
    ending_range = ingredient_range_arr[1]
    fresh_range_arr.append({
       'start': int(starting_range),
       'end': int(ending_range)
    })

  # go through test ingredients
  for test_ingredient in test_ingredients:
     ingredient_num = int(test_ingredient)

     for range in fresh_range_arr:
        if ingredient_num >= range['start'] and ingredient_num <= range['end']:
           fresh_count += 1
           break

  return fresh_count
