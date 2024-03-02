func carPooling(trips [][]int, capacity int) bool {
    d := map[int]int{}
    for _, t := range trips {
        d[t[1]] += t[0]
        d[t[2]] -= t[0]
    }
    keys := make([]int, 0, len(d))
    for k := range d {
        keys = append(keys, k)
    }
    slices.Sort(keys)
    s := 0
    for _, k := range keys {
        s += d[k]
        if s > capacity {
            return false
        }
    }
    return true
}