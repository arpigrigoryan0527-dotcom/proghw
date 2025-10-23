def binarysearch(l,x):
  n = len(l)
  s = 0
  h = n-1
  while s<=h:
    i = (s+h)//2
    if l[i]==x:
      return i
    elif l[i] < x:
      s = i+1
    else:
      h = i-1
  return False

l = [2,5,8,12,16,23,38,56,72,91]
x = 23
print(linearsearch(l,x)