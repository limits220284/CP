func maxProduct(words []string) int {
    n := len(words)
    bits := make([]int, n)
    for i, word := range words {
        t := 0
        for _, c := range word {
            t |= 1 << (c - 'a')
        }
        bits[i] = t
    }
    ans := 0
    for i := 0; i < n; i ++ {
        for j := i + 1; j < n; j ++ {
            if bits[i] & bits[j] == 0 {
                ans = max(ans, len(words[i]) * len(words[j]))
            }
        }
    }
    return ans
}