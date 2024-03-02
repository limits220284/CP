func maximumNumberOfStringPairs(words []string) int {
    var ans int
    seen := [26][26]bool{}
    for _, s := range words {
        x, y := s[0] - 'a', s[1] - 'a'
        if seen[y][x] {
            ans += 1
        } else {
            seen[x][y] = true
        }
    }
    return ans
}