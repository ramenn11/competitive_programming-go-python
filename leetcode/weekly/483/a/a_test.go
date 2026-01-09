package main

import (
	"github.com/79354/leetcode-go/leetcode/testutil"
	"testing"
)

func Test_a(t *testing.T) {
	if err := testutil.RunLeetCodeFuncWithFile(t, largestEven, "a.txt", 0); err != nil {
		t.Fatal(err)
	}
}
// https://leetcode.com/contest/weekly-contest-483/problems/largest-even-number/
// https://leetcode.com/problems/largest-even-number/
