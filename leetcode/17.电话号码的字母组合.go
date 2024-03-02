func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{}
    }
    ans := []string{}
    path := ""
    n := len(digits)
    var dfs func(int)
    mp := map[byte]string{
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }
    dfs = func(start int) {
        if start == n {
            ans = append(ans, path)
            return
        }
        s := mp[digits[start]]
        fmt.Println(s)
        m := len(s)
        for i := 0; i < m; i++ {
            path += string(s[i])
            dfs(start + 1)
            path = path[: len(path) - 1] 
        }
    }
    dfs(0)
    return ans
}