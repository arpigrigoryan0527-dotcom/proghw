def interpolationsearch(l,x):
  n=len(l)
  s=0
  h=n-1
  while s<=h:
    pos = s+int((x-l[s])*(h-s)/(l[h]-l[s]))
    if l[pos] == x:
      return pos
    elif l[pos] > x:
      h = pos-1
    else:
      s = pos+1
  return False

l = [2,5,8,12,16,23,38,56,72,91]
x = 23
print(linearsearch(l,x)