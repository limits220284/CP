/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	hh := make(map[int]int)
	for i, v := range nums {
		if idx, ok := hh[target - v]; ok {
			return []int{idx, i}
		}
		hh[v] = i
	}
	return []int{}
}
// @lc code=end

