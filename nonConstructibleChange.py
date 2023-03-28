def nonConstructibleChange(arr):
  arr.sort()
  smallestChange = arr[0]
  for num in arr:
    if num != smallestChange + 1:
      return smallestChange + 1
    else:
      smallestChange = num + smallestChange

if __name__ == '__main__':
  print(nonConstructibleChange([10,8,16,33,22,3,5,6,7,4,2,17,14]))
