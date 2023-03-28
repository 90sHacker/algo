def numberSum(arr, target):
  arr.sort()
  left = 0
  right = len(arr) - 1

  pairs = []
  same = []
  flag = True
  count = 0

  while flag:
    if arr[left] + arr[right] == target:
      if (left == right) and (left not in same):
        count += 1
        same.append(left)
        pairs.append([arr[left], arr[right]])

      else:
        count += 2
        pairs.append([arr[left],arr[right]])

    if left < right:
      left += 1
    elif left == right:
      if right == 0:
        flag = False

      left = 0
      right -= 1

  print(pairs)
  print(same)
  return count


if __name__ == '__main__':
  print(numberSum([1,8,-3,0,1,3,-2,4,5], 6))
     
