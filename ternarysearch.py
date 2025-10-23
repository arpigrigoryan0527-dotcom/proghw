def ternarysearch(l,x):
  n = len(l)
  s = 0
  h = n-1
  while s<=h:
    d = (h - s) // 3
    m1 = s + d
    m2 = h - d
    if l[m1]==x:
      return m1
    elif l[m2]==x:
      return m2
    elif l[m1]<x<l[m2]:
      s = m1+1
      h = m2-1
    elif l[m1]>x:
      h = m1-1
    elif l[m2]<x:
      s = m2+1
  return False

l = [2,5,8,12,16,23,38,56,72,91]
x = 23
print(linearsearch(l,x)