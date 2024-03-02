func minOperations(nums []int, k int) int {
	p := 0
	// n := len(nums)
	for _, num := range nums {
		p ^= num
	}
	if p == k {
		return 0
	}
	p = p ^ k
	ct := 0
	for p > 0 {
		ct += p & 1
		p >>= 1
	}
	return ct
}