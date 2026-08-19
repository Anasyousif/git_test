package main

func getNameCounts(names []string) map[rune]map[string]int {
	result := make(map[rune]map[string]int) 

	for _, name := range names {
		if len(name) == 0 {
			continue
		}
		firstRune := []rune(name)[0]
		if result[firstRune] == nil {
			result[firstRune] = make(map[string]int)
		}
		result[firstRune][name]++
	}
	return result
}
