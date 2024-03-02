func lengthOfLongestSubstring(s string) int {
    l, r := 0, 0
    mp := map[byte]int{}
    ans := 0
    for r < len(s) {
        mp[s[r]] += 1
        for mp[s[r]] > 1 {
            mp[s[l]] -= 1
            l += 1
        } 
        ans = max(ans, r - l + 1)
        r += 1
    }
    return ans
}