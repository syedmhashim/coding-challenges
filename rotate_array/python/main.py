def rotate_array(nums, n):
  n = n % len(nums)
  index = -1
  r = n
  if n < 0:
    index = 0
    r = -n
  for i in range(r):
    e = nums.pop(index)
    if index == 0:
      nums.append(e)
    else:
      nums = [e] + nums
  return nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))