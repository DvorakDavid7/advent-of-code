package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

type Mapping map[string][]string

// https://go.dev/play/p/SmzvkDjYlb
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// https://go.dev/play/p/SmzvkDjYlb
func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)
	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}
	return result
}

func getStartingNodes(mapping Mapping) []string {
	var result []string
	for key := range mapping {
		if key[len(key)-1] == 'A' {
			result = append(result, key)
		}
	}
	return result
}

func solveRec(instructions string, instructionIndex int, position string, mapping Mapping) int {
	if position == "ZZZ" {
		return 0
	}

	if instructionIndex == len(instructions) {
		instructionIndex = 0
	}
	instruction := instructions[instructionIndex]

	if instruction == 'L' {
		i := instructionIndex + 1
		nextPos := mapping[position][0]
		return 1 + solveRec(instructions, i, nextPos, mapping)
	}

	if instruction == 'R' {
		i := instructionIndex + 1
		nextPos := mapping[position][1]
		return 1 + solveRec(instructions, i, nextPos, mapping)
	}
	return 0
}

func isEndingPosition(position string) bool {
	return position[len(position)-1] == 'Z'
}

func movePosition(position string, mapping Mapping, instruction rune) string {
	if instruction == 'L' {
		return mapping[position][0]
	}
	return mapping[position][1]
}

func numberOfStepsToEnd(position string, instructions string, instructionIndex int, mapping Mapping) int {
	currentPositoin := position
	var i int = 0
	for !isEndingPosition(currentPositoin) {
		if instructionIndex == int(len(instructions)) {
			instructionIndex = 0
		}
		instruction := instructions[instructionIndex]
		currentPositoin = movePosition(currentPositoin, mapping, rune(instruction))
		instructionIndex += 1
		i += 1
	}
	return i
}

func main() {
	bytes, _ := os.ReadFile("./input.txt")
	data := strings.Split(string(bytes), "\n")
	instructions := data[0]
	mapping := make(Mapping)

	for _, m := range data[2:] {
		lhs := strings.Split(m, " = ")[0]
		values := strings.Split(m, " = ")[1]
		values = strings.ReplaceAll(values, "(", "")
		values = strings.ReplaceAll(values, ")", "")
		left, right := strings.Split(values, ", ")[0], strings.Split(values, ", ")[1]

		mapping[lhs] = []string{left, right}
	}

	startings := getStartingNodes(mapping)
	sort.Strings(startings)

	var arr []int
	for _, starting := range startings {
		res := numberOfStepsToEnd(starting, instructions, 0, mapping)
		arr = append(arr, res)
	}
	fmt.Println(LCM(arr[0], arr[1], arr[1:]...))

	res1 := solveRec(instructions, 0, "AAA", mapping)
	fmt.Println(res1)
}
