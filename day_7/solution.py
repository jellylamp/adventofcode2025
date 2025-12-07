from collections import deque  # Import deque for efficient queue operations
import copy

def parse_input_2d(input_text):
  array2D = []
  with open(input_text, 'r') as f:
    for line in f.read().splitlines():
      array2D.append(list(line))
  return array2D

def print_map(grid):
  print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in grid]))

def part1(input_text):
  manifold_map = parse_input_2d(input_text)
  manifold_copy = copy.deepcopy(manifold_map)
  start_col_index = manifold_map[0].index('S')
  split_count = bfs(manifold_map, 0, start_col_index, manifold_copy)
  return split_count


# Define the BFS function
def bfs(manifold_map, start_row, start_col, map_copy):
  visited = []  # List to keep track of visited node ids
  queue = deque([{
    'id': create_node_id(start_row, start_col),
    'row_idx': start_row,
    'col_idx': start_col
  }])  # Initialize the queue with the starting node

  map_row_bound = len(manifold_map) - 1
  map_col_bound = len(manifold_map[0]) - 1
  split_count = 0

  while queue:  # While there are still nodes to process
    node = queue.popleft()  # Dequeue a node from the front of the queue
    # print('new node!', node)

    if node['id'] not in visited:  # Check if the node has been visited
      visited.append(node['id'])  # Mark the node as visited
      map_copy[node['row_idx']][node['col_idx']] = '|'
      # print_map(map_copy)

      # continue the trend to add to the queue
      # look at index directly below
      # if ., add it to the queue
      # if ^, add its neighbors to the queue
      if node['row_idx'] + 1 < map_row_bound:
        node_to_consider_row = node['row_idx'] + 1
        node_to_consider_col = node['col_idx']
        node_to_consider = manifold_map[node_to_consider_row][node_to_consider_col]
        # print(f"considering node [{node_to_consider_row}][{node_to_consider_col}]")

        if node_to_consider == '.':
          # print('node is .')
          node_to_consider_id = create_node_id(node_to_consider_row, node_to_consider_col)
          if node_to_consider_id not in visited:
            # print('not in visited, appending')
            queue.append({
              'id': node_to_consider_id,
              'row_idx': node_to_consider_row,
              'col_idx': node_to_consider_col
            })
        if node_to_consider == '^':
          # print('node is ^')
          # oh lawd we splittin, do the two items to the SIDE of the splitter
          split_count += 1

          # left side add to queue
          node_to_consider_row = node['row_idx'] + 1
          node_to_consider_col = node['col_idx'] - 1

          if node_to_consider_col < map_col_bound and node_to_consider_col >= 0:
            node_to_consider_id = create_node_id(node_to_consider_row, node_to_consider_col)
            if node_to_consider_id not in visited:
              queue.append({
                'id': node_to_consider_id,
                'row_idx': node_to_consider_row,
                'col_idx': node_to_consider_col
              })

          # right side add to queue
          node_to_consider_row = node['row_idx'] + 1
          node_to_consider_col = node['col_idx'] + 1

          if node_to_consider_col < map_col_bound and node_to_consider_col >= 0:
            node_to_consider_id = create_node_id(node_to_consider_row, node_to_consider_col)
            if node_to_consider_id not in visited:
              queue.append({
                'id': node_to_consider_id,
                'row_idx': node_to_consider_row,
                'col_idx': node_to_consider_col
              })
  return split_count

def part2(input_text):
  manifold_map = parse_input_2d(input_text)
  manifold_copy = copy.deepcopy(manifold_map)
  start_col_index = manifold_map[0].index('S')
  split_count = dfs_part2(manifold_map, 0, start_col_index)
  return split_count

def create_node_id(row, col):
  return f"r{str(row)} + c{str(col)}"


# Switch to a DFS so we can take advantage of memoization as my other code just hung
def dfs_part2(manifold_map, start_row, start_col):
    map_row_bound = len(manifold_map) - 1
    map_col_bound = len(manifold_map[0]) - 1
    memo = {}
    
    def dfs_recursive(row, col):
        # if we've taken the path, just jump to the answer instead of revisiting
        node_id = create_node_id(row, col)
        if node_id in memo:
          return memo[node_id]

        # reached the bottom row
        if row == map_row_bound:
            return 1
        
        path_count = 0
        
        # Look at the cell directly below
        if row + 1 <= map_row_bound:
            node_to_consider_row = row + 1
            node_to_consider_col = col
            node_to_consider = manifold_map[node_to_consider_row][node_to_consider_col]
            
            if node_to_consider == '.':
                # Continue straight down
                path_count += dfs_recursive(node_to_consider_row, node_to_consider_col)
            
            if node_to_consider == '^':
                # oh lawd we splittin, do the two items to the SIDE of the splitter
                # left side
                node_to_consider_row = row + 1
                node_to_consider_col = col - 1
                if node_to_consider_col < map_col_bound and node_to_consider_col >= 0:
                    path_count += dfs_recursive(node_to_consider_row, node_to_consider_col)
                
                # right side
                node_to_consider_row = row + 1
                node_to_consider_col = col + 1
                if node_to_consider_col >= 0 and node_to_consider_col <= map_col_bound:
                    path_count += dfs_recursive(node_to_consider_row, node_to_consider_col)

        # add the path to the memo
        memo[node_id] = path_count
        return path_count
    
    return dfs_recursive(start_row, start_col)