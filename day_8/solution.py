import math

def parse_input(input_text):
  with open(input_text) as my_file:
      array_of_strings = my_file.read().splitlines()
  return array_of_strings

def part1(input_text, stopping_junction_count):
  coord_list = parse_input(input_text)
  coord_map = []

  for coord in coord_list:
     coord_list = coord.split(',')
     coord_map.append({
        'id': get_coord_id(coord_list),
        'x': int(coord_list[0]),
        'y': int(coord_list[1]),
        'z': int(coord_list[2])
     })

  distance_list = []

  union_find = UnionFind()

  # Generate ALL unique pairs and their distances
  for i, coord1 in enumerate(coord_map):
    for j, coord2 in enumerate(coord_map):
      # Skip self and duplicate pairs
      if i >= j:
          continue
      
      distance = get_euclidean_distance(coord1, coord2)
      distance_list.append((distance, coord1, coord2))
  
  # sort distance_list by closest distance
  distance_list.sort(key=lambda x: x[0])

  connections_made = 0
  for distance, coord1, coord2 in distance_list:
    # print(f"{distance} between {coord1['id']} and {coord2['id']}\n")

    union_find.merge_groups(coord1['id'], coord2['id'])
    connections_made += 1
    
    # print(f"Connections made: {connections_made}")
    if connections_made >= stopping_junction_count:
      break

  # Then calculate the product of the largest three circuit counts  
  top_three_list = union_find.get_top_three_groups()

  return len(top_three_list[0]) * len(top_three_list[1]) * len(top_three_list[2])

def part2(input_text):
  coord_list = parse_input(input_text)
  coord_map = []

  for coord in coord_list:
     coord_list = coord.split(',')
     coord_map.append({
        'id': get_coord_id(coord_list),
        'x': int(coord_list[0]),
        'y': int(coord_list[1]),
        'z': int(coord_list[2])
     })

  distance_list = []

  union_find = UnionFind()

  # Generate ALL unique pairs and their distances
  for i, coord1 in enumerate(coord_map):
    for j, coord2 in enumerate(coord_map):
      # Skip self and duplicate pairs
      if i >= j:
          continue
      
      distance = get_euclidean_distance(coord1, coord2)
      distance_list.append((distance, coord1, coord2))
  
  # sort distance_list by closest distance
  distance_list.sort(key=lambda x: x[0])

  x_product = 0
  total_coords = len(coord_map)

  for distance, coord1, coord2 in distance_list:
      # print(f"{distance} between {coord1['id']} and {coord2['id']}\n")
      are_all_groups_merged = union_find.merge_groups_pt_2(coord1['id'], coord2['id'], total_coords)
      
      if not are_all_groups_merged:
          print(f"ALL GROUPS ARE MERGED", coord1, coord2)
          x_product = coord1['x'] * coord2['x']
          break

  return x_product



def get_euclidean_distance(coord1, coord2):
  distance = math.sqrt((coord1['x'] - coord2['x'])** 2 + (coord1['y'] - coord2['y'])** 2 + (coord1['z'] - coord2['z'])** 2)
  # print(f"distance between {coord1['id']} and {coord2['id']} is {distance}")

  return distance

def get_coord_id(coord_list):
  return f"x{coord_list[0]}y{coord_list[1]}z{coord_list[2]}"


# Disjoint sets that can be unioned together if they match
# https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
class UnionFind:
  def __init__(self):
    # Maps each item to its parent item (or itself if it's the only one)
    self.parent_map = {}

    # Tracks the tree height to keep merges efficient (path counting)
    self.tree_depth = {}

  def find(self, item):
    """Return the item's group, creating it if needed."""
    
    # If this item has never been seen, initialize it as its own circuit
    if item not in self.parent_map:
        self.parent_map[item] = item
        self.tree_depth[item] = 0
        return item

    # Path compression: optimization
    if self.parent_map[item] != item:
        self.parent_map[item] = self.find(self.parent_map[item])

    return self.parent_map[item]

  def merge_groups(self, item_a, item_b):
    root_a = self.find(item_a)
    root_b = self.find(item_b)

    # Already in the same group
    if root_a == root_b:
        return False

    # Attach the smaller-depth tree under the larger-depth tree
    if self.tree_depth[root_a] < self.tree_depth[root_b]:
        self.parent_map[root_a] = root_b
    elif self.tree_depth[root_a] > self.tree_depth[root_b]:
        self.parent_map[root_b] = root_a
    else:
        # Same depth: choose one root and increase its depth
        self.parent_map[root_b] = root_a
        self.tree_depth[root_a] += 1

    if self.get_groups() == 1:
       return True
    return False
  
  def merge_groups_pt_2(self, item_a, item_b, total_coords):
    root_a = self.find(item_a)
    root_b = self.find(item_b)

    if root_a == root_b:
        num_groups = self.get_groups()
        total_items = len(self.parent_map)
        
        # Check if ALL original coords are in one group
        if num_groups == 1 and total_items == total_coords:
            return False
        return True

    if self.tree_depth[root_a] < self.tree_depth[root_b]:
        self.parent_map[root_a] = root_b
    elif self.tree_depth[root_a] > self.tree_depth[root_b]:
        self.parent_map[root_b] = root_a
    else:
        self.parent_map[root_b] = root_a
        self.tree_depth[root_a] += 1

    num_groups = self.get_groups()
    total_items = len(self.parent_map)
    print(f"Merged! Groups: {num_groups}, Total items: {total_items}/{total_coords}")
    
    # Stop if everything is merged into 1 group AND all coords are present
    if num_groups == 1 and total_items == total_coords:
        return False
    else:
        return True

  def get_groups(self):
    groups = {}

    for item in self.parent_map:
      root = self.find(item)
      groups.setdefault(root, []).append(item)

    return len(groups)

  def get_top_three_groups(self):    
    groups = {}

    for item in self.parent_map:
      root = self.find(item)
      groups.setdefault(root, []).append(item)

    sorted_groups = sorted(groups.values(), key=len, reverse=True)
    print(sorted_groups)

    top_three = sorted_groups[:3]

    return top_three
