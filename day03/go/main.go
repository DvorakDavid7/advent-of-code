package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

type NumCoords struct {
	NumberValue string
	StartIndex  int
	LineNumber  int
}

type Coord struct {
	Line  int
	Index int
}

type Neighbor struct {
	Number string
	Symbol rune
	Coord  Coord
}

func chopFirstNumber(line string) string {
	result := ""
	for _, char := range line {
		if unicode.IsDigit(char) {
			result = result + string(char)
		} else {
			return result
		}
	}
	return result
}

func hasSymbol(line string) bool {
	for _, char := range line {
		if isSymbol(char) {
			return true
		}
	}
	return false
}

func normalizeRange(start, end, lineLen int) (int, int) {
	return normalizeStartIndex(start), normalizeEndIndex(end, lineLen)
}

func normalizeStartIndex(start int) int {
	if start < 0 {
		return 0
	}
	return start
}

func normalizeEndIndex(end, length int) int {
	if end > length {
		return length
	}
	return end
}

func isSymbol(ch rune) bool {
	if !unicode.IsDigit(ch) && ch != '.' {
		return true
	}
	return false
}

func isPartNumber(numCoords NumCoords, data []string) bool {
	start := numCoords.StartIndex
	end := numCoords.StartIndex + len(numCoords.NumberValue)
	line := data[numCoords.LineNumber]
	s, e := normalizeRange(start-1, end+1, len(line))
	aboveSymbol := false
	underSymbol := false

	// check line above
	if numCoords.LineNumber > 0 {
		aboveSymbol = hasSymbol(data[numCoords.LineNumber-1][s:e])
	}

	// check line under
	if numCoords.LineNumber < len(data)-1 {
		underSymbol = hasSymbol(data[numCoords.LineNumber+1][s:e])
	}

	// check sides
	right := normalizeEndIndex(end, len(line)-1)
	left := normalizeStartIndex(start - 1)
	rightSymbol := isSymbol(rune(line[right]))
	leftSymbol := isSymbol(rune(line[left]))

	return rightSymbol || leftSymbol || aboveSymbol || underSymbol
}

func getNeighbors(line string, lineNumber int, number string, startIndex int) []Neighbor {
	var result []Neighbor = []Neighbor{}

	for i, char := range line {
		if isSymbol(char) {
			neighbor := Neighbor{
				Number: number,
				Symbol: char,
				Coord: Coord{
					Line:  lineNumber,
					Index: startIndex + i,
				},
			}
			result = append(result, neighbor)
		}
	}

	return result
}

func getAllNeighbors(numCoords NumCoords, data []string) []Neighbor {
	start := numCoords.StartIndex
	end := numCoords.StartIndex + len(numCoords.NumberValue)
	line := data[numCoords.LineNumber]
	numStart, numEnd := normalizeRange(start-1, end+1, len(line))

	var result []Neighbor = []Neighbor{}

	// check line above
	if numCoords.LineNumber > 0 {
		n := getNeighbors(data[numCoords.LineNumber-1][numStart:numEnd], numCoords.LineNumber-1, numCoords.NumberValue, numStart)
		result = append(result, n...)
	}
	// check line under
	if numCoords.LineNumber < len(data)-1 {
		n := getNeighbors(data[numCoords.LineNumber+1][numStart:numEnd], numCoords.LineNumber+1, numCoords.NumberValue, numStart)
		result = append(result, n...)
	}

	// check sides
	right := normalizeEndIndex(end, len(line)-1)
	left := normalizeStartIndex(start - 1)
	isRightSymbol := isSymbol(rune(line[right]))
	isLeftSymbol := isSymbol(rune(line[left]))

	if isRightSymbol {
		result = append(result, Neighbor{
			Number: numCoords.NumberValue,
			Symbol: rune(line[right]),
			Coord: Coord{
				Line:  numCoords.LineNumber,
				Index: right,
			},
		})
	}

	if isLeftSymbol {
		result = append(result, Neighbor{
			Number: numCoords.NumberValue,
			Symbol: rune(line[left]),
			Coord: Coord{
				Line:  numCoords.LineNumber,
				Index: left,
			},
		})
	}

	return result
}

func findCorespondingNeighbor(neighbors []Neighbor, target Neighbor, currentIndex int) *Neighbor {
	for i, neighbor := range neighbors {
		if i == currentIndex {
			continue
		}

		if neighbor.Coord == target.Coord {
			return &neighbor
		}
	}
	return nil
}

func main() {
	bytes, _ := os.ReadFile("./input.txt")
	data := strings.Split(string(bytes), "\n")

	sumPart1 := 0
	sumPart2 := 0
	neighbors := []Neighbor{}
	for ln, line := range data {
		i := 0
		for i < len(line) {
			numStart := i
			if unicode.IsDigit(rune(line[i])) {
				num := chopFirstNumber(line[i:])
				numStart = i
				i = i + len(num)

				coords := NumCoords{
					NumberValue: num,
					StartIndex:  numStart,
					LineNumber:  ln,
				}
				partNumber := isPartNumber(coords, data)
				n := getAllNeighbors(coords, data)

				if partNumber {
					numInt, _ := strconv.Atoi(num)
					sumPart1 += numInt
				}

				neighbors = append(neighbors, n...)
			}
			i = i + 1
		}
	}

	for i, neighbor := range neighbors {
		if neighbor.Symbol != rune('*') {
			continue
		}
		corespondingNeighbor := findCorespondingNeighbor(neighbors, neighbor, i)
		if corespondingNeighbor != nil {
			first, _ := strconv.Atoi(corespondingNeighbor.Number)
			second, _ := strconv.Atoi(neighbor.Number)
			sumPart2 += first * second
		}
	}

	fmt.Println(sumPart1)
	fmt.Println(sumPart2 / 2) // I count each neighbor twice
}
