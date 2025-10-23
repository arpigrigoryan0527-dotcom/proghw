def shift_table(pattern):
  shift = {}
  m = len(pattern)
  for i in range(m - 2, -1, -1):
    if pattern[i] not in shift:
      shift[pattern[i]] = m - i - 1
  if pattern[-1] not in shift:
    shift[pattern[-1]] = m
  return shift

def boyer_moore(text, pattern):
  n, m = len(text), len(pattern)
  shift = shift_table(pattern)
  i = m - 1
  while i < n:
    if text[i] != pattern[-1]:
      i += shift.get(text[i], m)
    else:
      j = m - 2
      k = i - 1
      while j >= 0 and text[k] == pattern[j]:
        j -= 1
        k -= 1
      if j < 0:
        print(f"Find: {i - m + 1}")
        i += m
      else:
        i += shift.get(pattern[j], m)

text = "sdfjfd asdasd erdfasdkjf sdfsdfass asddasd"
pattern = "asd"
boyer_moore(text, pattern)
