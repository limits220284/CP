func closeStrings(word1 string, word2 string) bool {
    // 只需要判断字符出现的频率是否一样就可以
    m, n := len(word1), len(word2)
    if m != n {
        return false
    }
    arr1 := [26]int{}
    arr2 := [26]int{}
    mask1 := 0
    mask2 := 0
    for i := 0; i < n; i++ {
        arr1[word1[i]-'a'] += 1
        mask1 |= (1 << (word1[i]-'a'))
        arr2[word2[i]-'a'] += 1
        mask2 |= (1 << (word2[i]-'a'))
    }
    sort.Ints(arr1[:])
    sort.Ints(arr2[:])
    if mask1 != mask2 {
        return false
    }
    // Compare the frequency arrays
    for i := 0; i < 26; i++ {
        if arr1[i] != arr2[i] {
            return false
        }
    }

    return true
}
