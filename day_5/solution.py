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
       'count': ending_range - starting_range + 1,
       'checked': False,
       'overlap_count': 0
    })
    fresh_count += ending_range - starting_range + 1

  print("fresh count before removals", fresh_count)

  for current_ingredient in fresh_range_arr:
     for ingredient_to_check in fresh_range_arr:
      # skip yourself!
      if ingredient_to_check['index'] == current_ingredient['index']:
        current_ingredient['checked'] = True
        continue

      # we are comparing everything thats been compared to now
      if ingredient_to_check['checked'] == True:
         current_ingredient['checked'] = True
         continue

      # Determine if ranges overlap
      if is_overlapping(current_ingredient['start'], current_ingredient['end'], ingredient_to_check['start'], ingredient_to_check['end']):
        # if they do by how much?
        print(f"range {current_ingredient['range']} overlaps {ingredient_to_check['range']}")
        num_to_remove = count_overlapped(current_ingredient['start'], current_ingredient['end'], ingredient_to_check['start'], ingredient_to_check['end'])
        
        # update the overlap count for the ingredient to check
        current_ingredient['overlap_count'] = current_ingredient['overlap_count'] + num_to_remove

        # mark as checked so we dont double compare
        current_ingredient['checked'] = True

  for current_ingredient in fresh_range_arr:
    print('overlap count', current_ingredient['overlap_count'])
    if (current_ingredient['overlap_count'] > current_ingredient['count']):
      fresh_count = fresh_count - current_ingredient['count']
    else:
      fresh_count = fresh_count - current_ingredient['overlap_count']

    # print("removing overlapping ", num_to_remove)
    # fresh_count = fresh_count - num_to_remove


  return fresh_count

def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)

# subtract from fresh count the overlap
# think about it
# 10-14 = 5 count
# 12-18 = 7 count
# 12 count total but double counting; want 9
# 14-12 = 2 + 1 = 3
def count_overlapped(x1,x2,y1,y2):
   highest_start = max(x1,y1)
   lowest_end = min(x2,y2)
   return lowest_end - highest_start + 1
