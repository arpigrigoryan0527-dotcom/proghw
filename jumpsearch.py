def jumpsearch(l,x):
  n = len(l)
  step = int((n)**0.5)
  i=0
  while i<n:
    if l[i] == x:
      return i
    else:
      i+=step
  i-=step
  for i in range(i,n):
    if l[i]==x:
      return i
  return False

l = [2,5,8,12,16,23,38,56,72,91]
x = 23
print(linearsearch(l,x)