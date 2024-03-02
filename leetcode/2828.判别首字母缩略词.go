func isAcronym(words []string, s string) bool {
    ans := ""
    for _, word := range words {
        ans += string(word[0])
    }
    return ans == s
}