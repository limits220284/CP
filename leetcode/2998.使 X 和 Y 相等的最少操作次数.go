func minimumOperationsToMakeEqual(x int, y int) int {
    if x <= y {
		return y - x
	}
	h := []int{x}
	vis := make(map[int]bool)
	minn := x - y
	mxt := int(math.Max(float64((x/11+1)*11), float64((x/5+1)*5)))
	// mnt := int(math.Min(float64((x/11)*11), float64((x/5)*5)))
	ct := 0
	for len(h) > 0 {
		s := []int{}
		if ct >= minn {
			break
		}
		for _, v := range h {
			if v <= y {
				minn = int(math.Min(float64(minn), float64(ct+y-v)))
				continue
			}
			if v%11 == 0 {
				if _, ok := vis[v/11]; !ok {
					vis[v/11] = true
					s = append(s, v/11)
				}
			}
			if v%5 == 0 {
				if _, ok := vis[v/5]; !ok {
					vis[v/5] = true
					s = append(s, v/5)
				}
			}
			if v > mxt {
				continue
			}
			if _, ok := vis[v+1]; !ok {
				s = append(s, v+1)
				vis[v+1] = true
			}
			if _, ok := vis[v-1]; !ok {
				s = append(s, v-1)
				vis[v-1] = true
			}
		}
		h = s
		ct++
	}
	return minn
}