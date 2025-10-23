def prefix_function(pattern):
  length = len(pattern)
  table = [0] * length
  j = 0
  for i in range(1, length):
    while j > 0 and pattern[i] != pattern[j]:
      j = table[j - 1]
    if pattern[i] == pattern[j]:
      j += 1
      table[i] = j
  return table

def kmp_search(text, pattern):
  n, m = len(text), len(pattern)
  prefix = prefix_function(pattern)
  i = j = 0
  while i < n:
    if text[i] == pattern[j]:
      i += 1
      j += 1
      if j == m:
        print(f"Find: {i - m}")
        j = prefix[j - 1]
    else:
      if j > 0:
        j = prefix[j - 1]
      else:
        i += 1

text = "ababbabbabababbab"
pattern = "abab"
kmp_search(text, pattern)
