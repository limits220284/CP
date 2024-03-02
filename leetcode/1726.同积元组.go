func tupleSameProduct(nums []int) int {
    cnt := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            cnt[nums[i] * nums[j]] += 1
        }
    }
    ans := 0
    for _, v := range cnt {
        ans += v * (v - 1) * 4
    }    
    return ans
}