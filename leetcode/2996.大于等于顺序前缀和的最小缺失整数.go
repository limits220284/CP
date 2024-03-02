func missingInteger(nums []int) int {
    // 将切片转换为集合
	s := make(map[int]bool)
	for _, num := range nums {
		s[num] = true
	}

	// 找到连续整数序列的最大值
	mxn := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1]+1 {
			mxn += nums[i]
		} else {
			break
		}
	}

	// 找到缺失的整数
	for s[mxn] {
		mxn++
	}

	return mxn
}