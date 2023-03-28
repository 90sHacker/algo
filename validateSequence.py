from re import A


def validateSequence(arr, sequence):
  arrId = 0
  seqId = 0

  while arrId < len(arr) and seqId < len(sequence):
    if arr[arrId] == sequence[seqId]:
      seqId += 1
    arrId += 1
  return seqId == len(sequence)

if __name__ == '__main__':
  print(validateSequence([5,1,27,25,6,-1,8,10], [1,6,-1,10]))