func canWinNim(n int) bool {
    // 如果 n % 4 == 0 那么对方只要拿4 - 我拿的
    // 如果不是的话，只需要拿n % 4的，然后剩下跟着他拿即可
    return n % 4 != 0
}