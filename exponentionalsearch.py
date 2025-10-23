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

def exponentionalsearch(l,x):
  n = len(l)
  if l[0]==x:
    return 0
  i = 1
  j=0
  while i < n:
    if l[i]==x:
      return i
    elif l[i]>x:
      j = i//2+1
      if type(binarysearch(l[j:i],x)) == bool:
        return False
      else:
        return binarysearch(l[j:i],x) + j
    i*=2
  return binarysearch(l[i//2+1:],x)+i//2+1


l = [2,5,8,12,16,23,38,56,72,91]
x = 12
print(exponentionalsearch(l,x))