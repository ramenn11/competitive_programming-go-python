package main

import "strings"

func largestEven(s string) string {
	return strings.TrimRight(s, "1")
}
