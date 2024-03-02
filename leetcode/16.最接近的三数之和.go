func threeSumClosest(nums []int, target int) int {
    // 枚举两维，然后左边维护一个有序列表，然后在有序列表里二分
    n := len(nums)
    sort.Ints(nums)
    ans := math.MaxInt
    for first := 0; first < n; first += 1 {
        if first > 0 && nums[first] == nums[first - 1] {
            continue
        }
        third, second := n - 1, first + 1
        for second < third {
            sum := nums[first] + nums[second] + nums[third]
            if sum == target {
                return target
            }
            if abs(sum - target) < abs(ans - target) {
                ans = sum
            }
            if sum > target {
                k0 := third - 1
                for second < k0 && nums[k0] == nums[third] {
                    k0 -= 1
                }
                third = k0
            } else {
                j0 := second + 1
                for j0 < third && nums[j0] == nums[second] {
                    j0 += 1
                }
                second = j0
            }
        }
    }
    return ans
}
func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}