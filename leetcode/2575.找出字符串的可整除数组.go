func divisibilityArray(word string, m int) []int {
    n := len(word)
    div := make([]int, n)
    t := 0
    for i := 0; i < n; i ++ {
        t = t * 10 + int(word[i] - '0')
        if t % m == 0 {
            div[i] = 1
        }
        t %= m
    }
    return div
}