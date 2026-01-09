package main

import "slices"

func wordSquares(words []string) (ans [][]string) {
	slices.Sort(words)

	path := [4]int{}
	onPath := make([]bool, len(words))

	var dfs func(int)
	dfs = func(i int) {
		if i == 4 {
			top := words[path[0]]
			left := words[path[1]]
			right := words[path[2]]
			bottom := words[path[3]]
			if top[0] == left[0] && top[3] == right[0] && bottom[0] == left[3] && bottom[3] == right[3] {
				ans = append(ans, []string{top, left, right, bottom})
			}
			return
		}

		for j, on := range onPath {
			if !on {
				path[i] = j     
				onPath[j] = true
				dfs(i + 1)
				onPath[j] = false
			}
		}
	}

	dfs(0)
	return
}
