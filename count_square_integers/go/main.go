package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	var a int32 = 465868129
	var b int32 = 988379794
	squares(a, b)
}

func squares(a int32, b int32) {
	start := time.Now()
	aSqrt := int(math.Ceil(math.Sqrt(float64(a))))
	bSqrt := int(math.Floor(math.Sqrt(float64(b))))
	var sqrtIntCount int
	for i := aSqrt; i <= bSqrt; i++ {
		if i*i <= int(b) {
			sqrtIntCount++
		}
	}
	fmt.Println(sqrtIntCount)
	fmt.Println(-time.Until(start))
}
