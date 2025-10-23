def naive_search(text, pattern):
  text_len = len(text)
  pattern_len = len(pattern)
  for start in range(text_len - pattern_len + 1):
    match = True
    for j in range(pattern_len):
      if text[start + j] != pattern[j]:
        match = False
        break
    if match:
        print(f"Find: {start}")

t = "aaabbababbabbabababbab"
p = "abbab"
naive_search(t, p)