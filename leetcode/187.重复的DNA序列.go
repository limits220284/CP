const L = 10
func findRepeatedDnaSequences(s string) []string {
    //滑动窗口
    ans := []string {}
    cnt := map[string]int{}
    for i := 0; i <= len(s) - L; i++ {
        sub := s[i: i + L]
        cnt[sub] += 1
        if cnt[sub] == 2 {
            ans = append(ans, sub)
        }
    }
    return ans
}