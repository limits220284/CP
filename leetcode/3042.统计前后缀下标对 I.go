func countPrefixSuffixPairs(words []string) int {
    ans := 0
    n := len(words)
    for i := 0; i < n; i ++ {
        for j := i + 1; j < n; j ++ {
            if strings.HasPrefix(words[j], words[i]) && strings.HasSuffix(words[j], words[i]) {
                ans += 1
            }
        }
    }
    return ans
}