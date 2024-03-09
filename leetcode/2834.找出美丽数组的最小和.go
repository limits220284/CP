func minimumPossibleSum(n int, target int) int {
    MOD := 1000_000_007
    k := target / 2
    if k > n {
        k = n
    }
    d := n - k
    return ((1 + k) * k / 2 + max(0, (target + target + d - 1) * d / 2)) % MOD
}