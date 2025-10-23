def linearsearch(l,x):
  n = len(l)
  for i in range(n):
    if l[i]==x:
      return i
  return False

l = [2,5,8,12,16,23,38,56,72,91]
x = 23
print(linearsearch(l,x)