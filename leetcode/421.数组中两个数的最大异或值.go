func findMaximumXOR(nums []int) int {
    ans := 0
    highBit := bits.Len(uint(slices.Max(nums))) - 1
    vis := map[int]bool{}
    mask := 0
    for i := highBit; i >= 0; i-- {
        clear(vis)
        mask |= 1 << i
        newAns := ans | 1 << i
        for _, x := range nums {
            x &= mask
            if vis[newAns ^ x] {
                ans = newAns
                break
            }
            vis[x] = true
        }
    }
    return ans
}