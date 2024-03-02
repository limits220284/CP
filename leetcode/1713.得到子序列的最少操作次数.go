func minOperations(target []int, arr []int) int {
    // 核心思想是将arr中的元素转成target的下标，如果target在arr中存在一部分
    // 那么存在的一部分一定是下标单调递增的
    // 所以在arr中找最长递增子序列即可
    n := len(target)
    pos := make(map[int]int, n)
    for i, val := range target {
        pos[val] = i
    }
    d := []int{}
    for _, val := range arr {
        if idx, has := pos[val]; has {
            if p := sort.SearchInts(d, idx); p < len(d) {
                d[p] = idx
            } else {
                d = append(d, idx)
            }
        }
    }
    return n - len(d)
}