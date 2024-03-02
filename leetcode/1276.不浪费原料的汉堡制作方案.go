func numOfBurgers(tomatoSlices int, cheeseSlices int) []int {
    x := tomatoSlices - 2 * cheeseSlices
    if x < 0 || x % 2 == 1 || cheeseSlices - x / 2 < 0 {
        return nil
    }
    return []int{x / 2, cheeseSlices - x / 2}
}