func splitArray(nums []int, k int) int {
    check := func (mid int) bool {
        tot := 0
        cnt := 0
        for _, x := range nums {
            if x > mid {
                return false
            }
            if tot + x <= mid {
                tot += x
            } else {
                tot = x
                cnt += 1
            }
        }
        return cnt + 1 <= k
    }
    l, r := 0, int(1e12)
    for l < r {
        mid := (l + r) / 2
        if check(mid) {
            r = mid
        } else {
            l = mid + 1
        }
    }
    return l
}