package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
	"sync"
)

type Filter struct {
	name      string
	intervals [][]uint64
}

func parseIntervals(intervals string) []uint64 {
	i := strings.Split(intervals, " ")
	dst, _ := strconv.ParseUint(i[0], 10, 64)
	src, _ := strconv.ParseUint(i[1], 10, 64)
	len, _ := strconv.ParseUint(i[2], 10, 64)
	return []uint64{uint64(dst), uint64(src), uint64(len)}
}

func parseIntevalList(intervalList []string) [][]uint64 {
	var result [][]uint64
	for _, line := range intervalList {
		arr := parseIntervals(line)
		result = append(result, arr)
	}
	return result
}

func newFilter(name string, intervalsList []string) Filter {
	return Filter{
		name:      name,
		intervals: parseIntevalList(intervalsList),
	}
}

func (f Filter) getMapping(value uint64) uint64 {
	for _, interval := range f.intervals {
		dst, src, len := interval[0], interval[1], interval[2]
		if src <= value && value < src+len {
			return dst + (value - src)
		}
	}
	return value
}

func parseSeeds(seedsLine string) []uint64 {
	var result []uint64
	values := strings.Split(seedsLine, " ")[1:]
	for _, value := range values {
		s, _ := strconv.ParseUint(value, 10, 64)
		result = append(result, uint64(s))
	}
	return result
}

func parseSeedsIntervals(seedsLine string) [][]uint64 {
	var result [][]uint64
	values := strings.Split(seedsLine, " ")[1:]
	for i := 0; i+1 < len(values); i += 2 {
		sStr, eStr := values[i], values[i+1]
		s, _ := strconv.ParseUint(sStr, 10, 64)
		e, _ := strconv.ParseUint(eStr, 10, 64)
		result = append(result, []uint64{uint64(s), uint64(e)})
	}
	return result
}

func goThrughFilters(filters []Filter, value uint64) uint64 {
	filteredValue := value
	for _, filter := range filters {
		filteredValue = filter.getMapping(filteredValue)
	}
	return filteredValue
}

func solveForInterval(filters []Filter, start uint64, end uint64, seedRange int, response chan uint64, wg *sync.WaitGroup) {
	var result uint64 = math.MaxUint64
	for start < end {
		res := goThrughFilters(filters, start)
		if res < result {
			result = res
		}
		start += 1
	}
	fmt.Printf("seed interval %d, result: %d\n", seedRange+1, result)
	wg.Done()
	response <- result
}

func part1(seeds []uint64, filters []Filter) {
	var result uint64 = math.MaxUint64
	for _, seed := range seeds {
		res := goThrughFilters(filters, seed)
		if res < result {
			result = res
		}
		fmt.Printf("seeds %d, result: %d\n", seed, result)
	}
	fmt.Println(result)
}

func part2(seedsIntervals [][]uint64, filters []Filter) {
	results := make(chan uint64, 100)
	wg := &sync.WaitGroup{}

	for i, seedInterval := range seedsIntervals {
		start := seedInterval[0]
		end := start + seedInterval[1]
		wg.Add(1)
		go solveForInterval(filters, start, end, i, results, wg)
	}
	wg.Wait()
	close(results)

	var r []uint64
	for result := range results {
		r = append(r, result)
	}
	fmt.Println(slices.Min(r))
}

func main() {
	bytes, _ := os.ReadFile("./input.txt")
	data := strings.Split(string(bytes), "\n")

	seeds := parseSeeds(data[0])
	seedsIntervals := parseSeedsIntervals(data[0])
	var filters []Filter

	lines := data[2:]
	for len(lines) > 0 {
		i := slices.Index(lines, "")
		var f []string
		if i == -1 {
			f = lines
			lines = []string{}
		} else {
			f = lines[0:i]
			lines = lines[i+1:]
		}
		filter := newFilter(f[0], f[1:])
		filters = append(filters, filter)
	}
	part1(seeds, filters)
	part2(seedsIntervals, filters)
}
