// 筛一下1e7以内的质数
func init () {
    
}
func mostFrequentPrime(mat [][]int) int {
    m, n := len(mat), len(mat[0])
    // 固定一个方向
    nums := make(map[int]int)
    check := func (x, y int) bool {
        if 0 <= x && x < m && 0 <= y && y < n {
            return true
        }
        return false
    }
    // 东北
    for i := 0; i < m; i ++ {
        for j := 0; j < n; j ++ {
            num := 0
            x, y := i, j
            for check(x, y) {
                num = num * 10 + mat[x][y]
                x -= 1
                y += 1
                nums[num] += 1
                nums[reverseNumber(num)] += 1
            }
        }
    }
    // 东
    for i := 0; i < m; i ++ {
        for j := 0; j < n; j ++ {
            num := 0
            x, y := i, j
            for check(x, y) {
                num = num * 10 + mat[x][y]
                y += 1
                nums[num] += 1
                nums[reverseNumber(num)] += 1

            }
        }
    }
    // 东南
    for i := 0; i < m; i ++ {
        for j := 0; j < n; j ++ {
            num := 0
            x, y := i, j
            for check(x, y) {
                num = num * 10 + mat[x][y]
                x += 1
                y += 1
                nums[num] += 1
                nums[reverseNumber(num)] += 1

            }
        }
    }
    // 南
    for i := 0; i < m; i ++ {
        for j := 0; j < n; j ++ {
            num := 0
            x, y := i, j
            for check(x, y) {
                num = num * 10 + mat[x][y]
                x += 1
                nums[num] += 1
                nums[reverseNumber(num)] += 1
            }
        }
    }
    // 判断是不是质数
    isPrime := func (num int) bool {
        for i := 2; i <= num / i; i ++ {
            if num % i == 0 {
                return false
            }
        }
        return true
    }
    ans := -1
    cnt := 0
    for k, v := range nums {
        if k <= 10 {
            continue
        }
        if isPrime(k) {
            if v > cnt {
                cnt = v
                ans = k
            } else if v == cnt {
                ans = max(ans, k)
            }
        }
    }
    return ans
}

func reverseNumber(n int) int {
	reversed := 0
	for n != 0 {
		digit := n % 10
		reversed = reversed*10 + digit
		n /= 10
	}
	return reversed
}