package main
import (
	"strings"
)

func countDistinctWords(messages []string) int {
	distinctWords := make(map[string]bool) 

	for _, msg := range messages {
		words := strings.Fields(msg)
		for _, word := range words {
			lowerWord := strings.ToLower(word)
			distinctWords[lowerWord] = true
		}
	}
	return len(distinctWords)
}
