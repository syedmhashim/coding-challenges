package main

import "fmt"

func twoSums(nums []int, target int) [][]int {
	var result [][]int
	numsSet := make(map[int]struct{})
	numsSet[nums[0]] = struct{}{}
	for i := 1; i < len(nums); i++ {
		if _, ok := numsSet[nums[i]]; ok {
			continue
		}
		if _, ok := numsSet[target-nums[i]]; ok {
			result = append(result, []int{target - nums[i], nums[i]})
		}
		numsSet[nums[i]] = struct{}{}
	}
	return result
}

func main() {
	target := 7
	nums := []int{3, 5, 2, -4, 8, 5, 11}
	fmt.Println(twoSums(nums, target))
}

// func twoSums(nums []int, target int) []int {
// 	map_of_values := make(map[int]int)
// 	length_of_num := len(nums)
// 	map_of_values[nums[0]] = 0
// 	for i := 1; i < length_of_num; i++ {
// 		if _, ok := map_of_values[target-nums[i]]; ok {
// 			return []int{map_of_values[target-nums[i]], i}
// 		}
// 		map_of_values[nums[i]] = i
// 	}
// 	return []int{-1, -1}
// }
