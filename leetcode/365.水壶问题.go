// 3 5
// 0 5
// 3 2
// 2 0
// 2 5
// 3 4
// 如果都是偶数，那么一定搞不出奇数
// 奇 偶 
func canMeasureWater(x int, y int, z int) bool {
    if x + y < z {
        return false
    }
    if x == 0 || y == 0 {
        return z == 0 || x + y == z
    }
    return z % gcd(x, y) == 0
}
func gcd(x, y int) int {
    if y == 0 {
        return x
    }
    return gcd(y, x % y)
}