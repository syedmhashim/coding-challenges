import math

def binary_search(nums, target):
  size = len(nums)
  if size == 0:
    return -1
  mid_index = math.floor(size/2)
  mid = nums[mid_index]
  if target == mid:
    return mid_index
  if target > mid:
    res = binary_search(nums[mid_index+1:], target)
    return -1 if res == -1 else mid_index + 1 + res
  if target < mid:
    return binary_search(nums[:mid_index], target)
  return -1

print(binary_search([1,2,3,4,5,6,7,8,10,15], 5))