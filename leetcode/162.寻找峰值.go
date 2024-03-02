func findPeakElement(nums []int) int {
    n := len(nums)
    get := func(i int) int {
        if i == -1 || i == n {
            return math.MinInt64
        }
        return nums[i]
    }
    l, r := 0, n - 1
    for {
        mid := (l + r) / 2
        if get(mid - 1) < get(mid) &&  get(mid) > get(mid + 1) {
            return mid
        }
        if get(mid) < get(mid + 1) {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
}