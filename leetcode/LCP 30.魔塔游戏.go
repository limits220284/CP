func magicTower(nums []int) (ans int) {
    sum := 0
    for _, x := range nums {
        sum += x
    }
    if sum < 0 {
        return -1
    }
    hp := 1
    h := &minHeap{}
    for _, x := range nums {
        if x < 0 {
            heap.Push(h, x)
        }
        hp += x
        if hp < 1 {
            hp -= heap.Pop(h).(int)
            ans += 1
        }
    }
    return 
}
type minHeap struct {
    sort.IntSlice // 继承Len, Less, Swap
}
func (h *minHeap) Push(v any) {
    h.IntSlice = append(h.IntSlice, v.(int))
}
func (h *minHeap) Pop() any {
    a := h.IntSlice
    v := a[len(a) - 1]
    h.IntSlice = a[:len(a) - 1]
    return v
}