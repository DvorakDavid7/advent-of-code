package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func part1() {
	bytes, _ := os.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	sum := 0
	for _, line := range lines {
		var digits []int
		for _, char := range line {
			if num, err := strconv.Atoi(string(char)); err == nil {
				digits = append(digits, num)
			}
		}
		val, _ := strconv.Atoi(fmt.Sprintf("%d%d", digits[0], digits[len(digits)-1]))
		sum = sum + val
	}
	fmt.Println(sum)
}

var words = []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

func part2() {
	bytes, _ := os.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")
	sum := 0
	for _, line := range lines {
		var digits []int
		for i, char := range line {
			if num, err := strconv.Atoi(string(char)); err == nil {
				digits = append(digits, num)
			}

			for d, word := range words {
				if strings.HasPrefix(line[i:], word) {
					digits = append(digits, d+1)
				}
			}
		}
		val, _ := strconv.Atoi(fmt.Sprintf("%d%d", digits[0], digits[len(digits)-1]))
		sum = sum + val
	}

	fmt.Println(sum)
}

func main() {
	part2()
}
