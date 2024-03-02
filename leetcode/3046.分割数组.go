func isPossibleToSplit(nums []int) bool {
    mp := make(map[int]int)
    for _, v := range nums {
        mp[v] += 1
        if mp[v] >= 3 {
            return false
        }
    }
    return true
}