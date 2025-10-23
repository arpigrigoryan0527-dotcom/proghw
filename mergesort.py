def merge_sorted(a, b):
  result = []
  p1, p2 = 0, 0
  while p1 < len(a) and p2 < len(b):
    if a[p1] < b[p2]:
      result.append(a[p1])
      p1 += 1
    else:
      result.append(b[p2])
      p2 += 1
  if p1 < len(a):
    result.extend(a[p1:])
  if p2 < len(b):
    result.extend(b[p2:])
  return result


def merge_sort(arr):
  n = len(arr)
  if n <= 1:
    return arr
  mid = n // 2
  left_half = merge_sort(arr[:mid])
  right_half = merge_sort(arr[mid:])
  return merge_sorted(left_half, right_half)


numbers = [4, 5, 7, 1, 2, 8, 6]
print(merge_sort(numbers))