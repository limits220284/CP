func vowelStrings(words []string, left int, right int) int {
    ans := 0
    yuan := map[byte]bool{'a':true, 'e':true, 'i':true, 'o':true, 'u':true}
    for _, word := range(words[left: right + 1]) {
        if yuan[word[0]] && yuan[word[len(word) - 1]] {
            ans += 1
        }
    }
    return ans
}