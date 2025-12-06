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

def part2(input_text):
  fresh_ingredients, test_ingredients = parse_input(input_text)
  fresh_range_arr = []
  fresh_count = 0
  fresh_ingredients_set = set(fresh_ingredients)
  
  # make a range dictionary
  for index, ingredient_range in enumerate(fresh_ingredients_set):
     # parse out -
    ingredient_range_arr = ingredient_range.split('-')
    starting_range = int(ingredient_range_arr[0])
    ending_range = int(ingredient_range_arr[1])
    fresh_range_arr.append({
       'index': index,
       'range': str(ingredient_range),
       'start': starting_range,
       'end': ending_range,
       'count': ending_range - starting_range + 1
    })
  
  # Sort ranges by start position
  fresh_range_arr.sort(key=lambda x: x['start'])
  
  # Merge overlapping ranges
  merged_ranges = []
  for current_ingredient in fresh_range_arr:
    # Create new range only if no overlap (start > last end)
    if not merged_ranges or current_ingredient['start'] > merged_ranges[-1]['end']:
      merged_ranges.append({
        'start': current_ingredient['start'],
        'end': current_ingredient['end']
      })
    else:
      # Ranges overlap, so merge by extending the end if needed
      merged_ranges[-1]['end'] = max(merged_ranges[-1]['end'], current_ingredient['end'])
  
  # Count total numbers in all merged ranges
  for merged_range in merged_ranges:
    fresh_count += merged_range['end'] - merged_range['start'] + 1
  
  return fresh_count

def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)

def count_overlapped(x1,x2,y1,y2):
   highest_start = max(x1,y1)
   lowest_end = min(x2,y2)
   return lowest_end - highest_start + 1