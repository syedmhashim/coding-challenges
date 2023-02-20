def topK(s, k):
  char2count = dict()
  for char in s:
    if char in char2count:
      char2count[char] += 1
    else:
      char2count[char] = 1
  counts = list(char2count.values())
  counts.sort(reverse=True)
  counts = counts[:k]
  output = list()
  for char,count in char2count.items():
    if count in counts:
      output.append(char)
      counts.remove(count)
    if len(output) == k:
      return output

if __name__ == "__main__":
    k = 3
    test_cases = [
        "aabreijkje121a",
        "aabbcccdddd"
    ]
    print(f"K: {k}")
    for i in range(len(test_cases)):
        print("Test case:")
        print(test_cases[i])
        
        print("Result:")
        print(topK(test_cases[i], k))