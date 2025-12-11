
def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines() 
  return array_of_strings

def part1(input_text):
  device_directions_list = parse_input(input_text)
  device_map = {}
  
  for device_directions in device_directions_list:
     device_list = device_directions.split(':')
     device_map[device_list[0]] = device_list[1][1:].split(' ')

  split_count = dfs(device_map, 'you')
  return split_count

def create_node_id(row, col):
  return f"r{str(row)} + c{str(col)}"


def dfs(device_map, device_to_search):
  memo = {}
  
  def dfs_recursive(device_to_search):
    if device_to_search in memo:
      print(f"found {device_to_search} in memo, returning {memo[device_to_search]}")
      return memo[device_to_search]
    
    print('device to search', device_to_search)
    path_count = 0
    device_children = device_map[device_to_search]
    
    for child in device_children:
      if child == 'out':
        path_count += 1
      else:
        path_count += dfs_recursive(child)
    
    print(f"adding {device_to_search} to memo with count {path_count}")
    memo[device_to_search] = path_count
    return path_count
  
  return dfs_recursive(device_to_search)


def part2(input_text):
  device_directions_list = parse_input(input_text)
  device_map = {}
  
  for device_directions in device_directions_list:
     device_list = device_directions.split(':')
     device_map[device_list[0]] = device_list[1][1:].split(' ')

  split_count = dfs_part2(device_map, 'svr', False, False)
  return split_count


def dfs_part2(device_map, device_to_search, hit_dac, hit_fft):
  memo = {}
  
  def dfs_recursive(device_to_search, hit_dac, hit_fft):
    key = (device_to_search, hit_dac, hit_fft)
    if key in memo:
      return memo[key]
    
    path_count = 0
    device_children = device_map[device_to_search]

    for child in device_children:
      if child == 'out' and hit_dac and hit_fft:
        path_count += 1
        continue

      if child != 'out':
        new_hit_dac = hit_dac or (child == 'dac')
        new_hit_fft = hit_fft or (child == 'fft')
        path_count += dfs_recursive(child, new_hit_dac, new_hit_fft)

    # If no more children but we have both DAC/FFT, this path is successful
    if path_count == 0 and hit_dac and hit_fft:
      path_count = 1

    memo[key] = path_count
    return path_count
  
  return dfs_recursive(device_to_search, hit_dac, hit_fft)