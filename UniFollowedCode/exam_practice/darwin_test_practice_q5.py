def shift_coordinates (nested_list, offset):
  results = []

  for i in nested_list:
    new_list = []
    for coordinate in i:
      new_coord = [coordinate[0] + offset[0], coordinate[1] + offset[1]]
      new_list.append(new_coord)
    
    results.append(new_list)

  return results


nested_list = [[[5, 1], [-2, 3]], [[0, 1], [-2, 3]],[[11, 0], [3, 3]]]
offset = (3, -2)
print(shift_coordinates(nested_list, offset))
#output: [[[8, -1], [1, 1]], [[3, -1], [1, 1]], [[14, -2], [6, 1]]]  