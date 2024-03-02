func minimumPerimeter(neededApples int64) int64 {
    n := int64(1)
    for 2 * n * (n + 1) * (2 * n + 1) < neededApples {
        n++
    }
    return n * 8
}
