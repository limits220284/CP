func earliestSecondToMarkIndices(nums []int, ci []int) int {
    // 问题在于当前的操作是什么
    // 如果存在没有消除完毕的1，那么可以消除，并且可以标志当前秒数对应的位置
    // 如果当前秒数对应的位置不是零，那么就判断是否要减1，如果没有1，就不做
    // 一种贪心的思路就是，如果能够标志，就优先标志，减1反正什么时候都能做，但是怎么减1呢？
    // 标志又该怎么标志呢
    // 容易出现一种情况，就是需要提前减去某个位置的1，然后等到那个点之后，直接标志，
    // 否则后面再也不会出现这种1了
    // 2000可以双重循环
    // 二分思路是正确的
    // 但是check函数怎么表示
    // 如果是二分的话，那么最后一秒一定是标记最后一个为零的数字
    // 那么该数字之前的相同的数字，都是处于减1的操作或者不变的操作
    // 
    n, m := len(nums), len(ci)
    check := func(mid int) bool {
        chk := make([]bool, n + 1)
        q := n
        rst := 0
        for i := mid; i >= 1; i -- {
            u := ci[i - 1]
            if !chk[u] {
                chk[u] = true
                q -= 1
                rst += nums[u - 1]
            } else {
                rst = max(rst - 1, 0)
            }
        }
        return q == 0 && rst == 0
    }
    l, r := 0, m
    for l < r {
        mid := (l + r) / 2
        if check(mid) {
            r = mid
        } else {
            l = mid + 1
        }
    }
    if check(l) == false {
        return -1
    }
    return l
}