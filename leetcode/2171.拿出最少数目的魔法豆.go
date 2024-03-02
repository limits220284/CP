func minimumRemoval(beans []int) int64 {
    n := len(beans)
    sort.Ints(beans)
    total := int64(0)
    for _, bean := range beans {
        total += int64(bean)
    }
    res := total
    for i := 0; i < n; i ++ {
        res = min(res, total - int64(beans[i]) * int64(n - i))
    }
    return res
}