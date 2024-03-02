func isPalindrome(x int) bool {
    // 直接将数字反转
    xc := x
    rev := 0
    for x > 0 {
        rev = rev * 10 + x % 10
        x /= 10
    }
    fmt.Println(x)
    return xc == rev 
}