# O(nlog(n)) time / O(n) space
# def sortedSquareArray(arr):
#   squareArray = [0 for _ in arr]

#   for i in range(len(arr)):
#     squareValue = arr[i] * arr[i]
#     squareArray[i] = squareValue
  
#   squareArray.sort()
#   return squareArray

#O(n) time / O(n) space
def sortedSquareArray(arr):
  squareArray = [0 for _ in arr]

  smallValueIdx = 0
  largeValueIdx = len(arr) - 1

  for i in reversed(range(len(arr))):
    if abs(arr[smallValueIdx]) < abs(arr[largeValueIdx]):
      squareArray[i] = arr[largeValueIdx] * arr[largeValueIdx]
      largeValueIdx -= 1
    else:
      squareArray[i] = arr[smallValueIdx] * arr[smallValueIdx]
      smallValueIdx += 1
  
  return squareArray


if __name__ == '__main__':
  print(sortedSquareArray([-2, -3, -5, 4, 7, 8, 10]))

