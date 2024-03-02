func splitWordsBySeparator(words []string, separator byte) []string {
    var res []string
    for _, word := range words {
        subs := strings.Split(word, string([]byte{separator}))
        for _, sub := range subs {
            if len(sub) > 0 {
                res = append(res, sub)
            }
        }
    }
    return res
}
