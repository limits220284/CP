func longestCommonPrefix(strs []string) string {
    i := 0 // 表示从头开始
    m := math.MaxInt
    for _, x := range strs {
        m = min(m, len(x))
    }
    ans := ""
    for i < m {
        for j := 1; j < len(strs); j++ {
            if strs[j][i] != strs[0][i] {
                return ans
            }
        }
        ans += string(strs[0][i])
        i += 1
    }
    return ans
}