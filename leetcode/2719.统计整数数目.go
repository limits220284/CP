func count(num1, num2 string, minSum, maxSum int) int {
	const mod = 1_000_000_007
	calc := func(s string) int {
		memo := make([][]int, len(s))
		for i := range memo {
			memo[i] = make([]int, min(9 * len(s), maxSum) + 1)
			for j := range memo[i] {
				memo[i][j] = -1
			}
		}
		var dfs func(int, int, bool) int
		dfs = func(i, sum int, isLimit bool) (res int) {
			if sum > maxSum { // 非法
				return
			}
			if i == len(s) {
				if sum >= minSum { // 合法
					return 1
				}
				return
			}
			if !isLimit {
				p := &memo[i][sum]
				if *p >= 0 {
					return *p
				}
				defer func() { *p = res }()
			}
			up := 9
			if isLimit {
				up = int(s[i] - '0')
			}
			for d := 0; d <= up; d++ { // 枚举当前数位填 d
				res = (res + dfs(i+1, sum+d, isLimit && d == up)) % mod
			}
			return
		}
		return dfs(0, 0, true)
	}
	ans := calc(num2) - calc(num1) + mod // 避免负数
	sum := 0
	for _, c := range num1 {
		sum += int(c - '0')
	}
	if minSum <= sum && sum <= maxSum { // num1 是合法的，补回来
		ans++
	}
	return ans % mod
}