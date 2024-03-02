func canPlaceFlowers(flowerbed []int, n int) bool {
    flowerbed = append(append([]int{0}, flowerbed...), 0)
    for i := 1; i < len(flowerbed) - 1; i++{
        if flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0{
            flowerbed[i] = 1
            n -= 1
        }
    }
    return n <= 0
}