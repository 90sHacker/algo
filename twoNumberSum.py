# 0(n) / O(1) space
def twoSum(arr, target):
  diff = 0
  for num in arr:
    diff = target - num
    if diff in arr:
      return [num, diff]
  return []

# O(n) / O(n) space 
def twoNumberSumHash(array, targetSum):
  tab = {}

  for num in array:
    match = targetSum - num
    if match in tab:
      return [match, num]
    else:
      tab[num] = True

  return []



# O(n(logn)) / 0(1) space
def twoNumberSum(array, targetSum):
  array.sort()
  left = 0
  right = len(array) - 1

  while left < right:
    currentSum = array[left] + array[right]

    if currentSum == targetSum:
      return [array[left], array[right]]
    elif currentSum < targetSum:
      left += 1
    elif currentSum > targetSum:
      right -= 1
  
  return []


if __name__ == "__main__":
  res0 = twoSum([3,2,4], 6)
  res1 = twoNumberSum([4, 5, 8, -1, 3, 2, 9], 14)
  res2 = twoNumberSumHash([4, 5, 8, -1, 3, 2, 9], 14)

  print(res0)
  print(res1)
  print(res2)