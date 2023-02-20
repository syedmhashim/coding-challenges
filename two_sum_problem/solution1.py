def two_sum_prob(t, arr_int):
  output = list()
  for i in range(len(arr_int) - 1):
    tmp_arr = arr_int[:i] + arr_int[i+1:]
    pair = [arr_int[i], t-arr_int[i]]
    pair.sort()
    if (t-arr_int[i] in tmp_arr) and (pair not in output):
      output.append(pair)
  return output

if __name__ == "__main__":
    target = 7
    test_cases = [
        [3,5,2,5,-4,8,10],
        [4,5,-2,8,3]
    ]
    
    print(f"target: {target}")
    for i in range(len(test_cases)):
        print("Test case:")
        print(test_cases[i])
        
        print("Result:")
        print(two_sum_prob(target, test_cases[i]))
