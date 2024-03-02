func isWinner(player1 []int, player2 []int) int {
    gao := func(player []int) int {
        ans := 0
        for i, c := range player {
            if (i > 0 && player[i - 1] == 10) || (i > 1 && player[i - 2] == 10) {
                ans += c * 2
            } else {
                ans += c
            }
        }
        return ans
    }
    ans1 := gao(player1)
    ans2 := gao(player2)
    if ans1 < ans2 {
        return 2
    } else if ans1 > ans2 {
        return 1
    }
    return 0
}