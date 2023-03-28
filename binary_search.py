def binary_search(num_list, find_num, left_idx, right_idx):
  if right_idx < left_idx:
    return -1

  mid_idx = (left_idx + right_idx) // 2
  if mid_idx >= len(num_list) or mid_idx < 0:
    return -1
    
  mid_num = num_list[mid_idx]

  if mid_num == find_num:
    return mid_idx

  if mid_num < find_num:
    left_idx = mid_idx + 1
  
  else:
    right_idx = mid_idx - 1

  return binary_search(num_list, find_num, left_idx, right_idx)
 
if __name__ == '__main__':
  num_list = [1,4,6,9,11,15,17,21,34,56]

  find_num = 9

  print(binary_search(num_list, find_num, 0, len(num_list)))