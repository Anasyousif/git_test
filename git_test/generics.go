package main

func getLast[T any](s []T) T {
	var zero T
	if len(s) == 0 {
		return zero
	}
	return s[len(s)-1]
}