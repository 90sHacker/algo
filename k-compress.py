def compress(word, k):
  #set start and stop index var
  #set len var
  #set counter

  #loop from start
  #if word[start] is 

  stack = []

  for ch in word:
    if stack and stack[-1][0] == ch:
      stack[-1][1] += 1
      print(stack[-1][1])
      if stack[-1][1] == k:
        stack.pop()
        print(stack)

    else:
      stack.append([ch, 1])
      print(stack)
  return ''.join([a * b for a,b in stack])

if __name__ == "__main__":
  print(compress('abbcccb', 3))
    