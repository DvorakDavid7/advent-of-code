package main

import (
	"fmt"
)

func doesBeatTheRecord(holdTime int, travelTime int, record int) bool {
	movingTime := travelTime - holdTime
	dest := movingTime * holdTime
	return dest > record
}

func solve(data [][]int) {
	var counts []int
	for _, record := range data {
		counter := 0
		for i := 1; i < record[0]; i++ {
			if doesBeatTheRecord(i, record[0], record[1]) {
				counter += 1
			}
		}
		counts = append(counts, counter)
	}

	result := 1
	for _, count := range counts {
		result *= count
	}
	fmt.Println(result)
}

func main() {
	// var tests = [][]int{
	// 	{7, 9}, {15, 40}, {30, 200},
	// }

	// var tests2 = [][]int{
	// 	{71530, 940200},
	// }

	var inputs = [][]int{
		{56, 546}, {97, 1927}, {78, 1131}, {75, 1139},
	}

	var inputs2 = [][]int{
		{56977875, 546192711311139},
	}

	solve(inputs)
	solve(inputs2)
}
