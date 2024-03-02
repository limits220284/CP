func canSeePersonsCount(heights []int) []int {
    n := len(heights)
	stack := make([]int, 0)
	res := make([]int, n)

	for i := n - 1; i >= 0; i-- {
		h := heights[i]
		for len(stack) > 0 && stack[len(stack)-1] <= h {
			stack = stack[:len(stack)-1]
            res[i] += 1;
		}
        if len(stack) > 0 {
            res[i] += 1;
        }
		stack = append(stack, h)
	}
	return res
}
