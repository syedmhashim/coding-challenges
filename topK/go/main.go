package main

import (
	"fmt"
	"sort"
)

func topK(s string, k int) []string {
	var res []string

	charToFrequency := make(map[string]int)
	for _, ru := range s {
		r := string(ru)
		_, ok := charToFrequency[r]
		if ok {
			charToFrequency[r] += 1
		} else {
			charToFrequency[r] = 1
		}
	}

	frequencyToChars := make(map[int][]string)
	var frequencies []int
	for k, v := range charToFrequency {
		if _, ok := frequencyToChars[v]; ok {
			frequencyToChars[v] = append(frequencyToChars[v], k)
		} else {
			frequencyToChars[v] = []string{k}
			frequencies = append(frequencies, v)
		}
	}

	sort.Ints(frequencies)

	for i := len(frequencies) - 1; i >= 0 && len(res) < k; i-- {
		res = append(res, frequencyToChars[frequencies[i]]...)
	}

	return res[:k]
}

func main() {
	fmt.Println(topK("aabreijkje121a", 3))

}
