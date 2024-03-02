func combine(n int, k int) (ans [][]int) {
	var temp []int
	dfs(&ans, temp, 1, n, k)
	return ans
}

func dfs(ans *[][]int, temp []int, index int, n int, k int) {
	if len(temp) == k {
		combination := make([]int, k)
		copy(combination, temp)
		*ans = append(*ans, combination)
		return
	}
	if index > n {
		return
	}
	for i := index; i <= n; i++ {
		temp = append(temp, i)
		dfs(ans, temp, i+1, n, k)
		temp = temp[:len(temp)-1]
	}
}