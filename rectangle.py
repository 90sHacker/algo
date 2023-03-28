MAX_INTEGER = 2147483647

def compute_area(x1, y1, x2, y2):
  width = abs(x2 - x1) 
  height = abs(y2 - y1)

  area = width * height

  return area

def intersection_area(k,l,m,n,p,q,r,s):
  iWidth = min([m,r]) - max([k,p])
  iHeight = min([n,s]) - max([l,q])

  iArea = iWidth * iHeight

  print('iArea is...', iArea)

  if iArea < 0:
    return 0

  return iArea 


def solution(k, l, m, n, p, q, r, s):
  areaOne = compute_area(k,l,m,n)
  areaTwo = compute_area(p,q,r,s)

  iarea = intersection_area(k,l,m,n,p,q,r,s)

  print('area is...', areaOne + areaTwo)

  totalArea = areaOne + areaTwo - iarea

  if totalArea > MAX_INTEGER:
    return -1

  return totalArea

if __name__ == '__main__':
  print(solution(-4,1,2,6,0,-1,4,3))
  print(solution(-4,1,2,6,0,3,4,7))
  print(solution(-4,1,2,6,4,3,0,7))
  print(solution(-4,1,2,6,-4,-1,0,3))
  print(solution(0,-1,4,3,-4,1,2,6))
  print(solution(0,0,10,10,2,2,4,4))



