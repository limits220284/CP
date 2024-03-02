func canConstruct(ransomNote string, magazine string) bool {
    rm := make(map[rune]int)
    for _, c := range ransomNote {
        rm[c] += 1
    }
    mm := make(map[rune]int)
    for _, c := range magazine {
        mm[c] += 1
    }
    for k, v := range rm {
        if v > mm[k] {
            return false
        }
    }
    return true
}