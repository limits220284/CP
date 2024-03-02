func maximumSum(nums []int) int {
    //hash表能够到达O(1)
    hsh := map[int]int{}
    ans := -1
    for _, x := range nums {
        t := x
        tot := 0
        for t > 0 {
            tot += t % 10
            t /= 10
        }
        if hsh[tot] != 0 {
            ans = max(ans, x + hsh[tot])
        }
        hsh[tot] = max(hsh[tot], x)
    }
    return ans
}