func countWords(words1 []string, words2 []string) int {
    // 统计字符串出现频率
    freq1 := make(map[string]int)
    freq2 := make(map[string]int)
    for _, w := range words1 {
        freq1[w]++
    }
    for _, w := range words2 {
        freq2[w]++
    }

    // 遍历 words1 出现的字符串并检查个数
    res := 0
    for w, cnt1 := range freq1 {
        if cnt1 == 1 && freq2[w] == 1 {
            res++
        }
    }
    return res
}
