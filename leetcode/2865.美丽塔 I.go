func maximumSumOfHeights(maxHeights []int) int64 {
    n := len(maxHeights)
    res := int64(0)
    for i := 0; i < n; i ++ {
        pre, psum := maxHeights[i], int64(maxHeights[i])
        for j := i - 1; j >= 0; j -- {
            pre = min(pre, maxHeights[j])
            psum += int64(pre)
        }
        suf := maxHeights[i]
        for j := i + 1; j < n; j++ {
            suf = min(suf, maxHeights[j])
            psum += int64(suf)
        }
        res = max(res, psum)
    }
    return res
}