func threeSumMulti(arr []int, target int) int {
    const MOD = 1e9 + 7
    n := len(arr)
    mp := make(map[int]int)
    ans := 0
    for j := 1; j < n; j++ {
        mp[arr[j - 1]] += 1
        for k := j + 1; k < n; k++ {
            t := target - arr[j] - arr[k]
            ans = (ans + mp[t]) % MOD
        }
    }
    return ans
}