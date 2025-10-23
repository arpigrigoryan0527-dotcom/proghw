def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  smaller, greater = [], []
  for x in arr:
    if x == pivot:
      continue
    if x < pivot:
      smaller.append(x)
    else:
      greater.append(x)
  return quick_sort(smaller) + [pivot] + quick_sort(greater)

numbers = [4, 7, 3, 15, 12, 9]
print(quick_sort(numbers))