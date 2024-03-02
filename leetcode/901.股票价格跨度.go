type StockSpanner struct {
    stack [][2]int
    n int
}


func Constructor() StockSpanner {
    return StockSpanner{}
}


func (s *StockSpanner) Next(price int) int {
    // 单调栈
    s.n += 1
    ans := -1
    for len(s.stack) > 0 && s.stack[len(s.stack) - 1][1] <= price {
        s.stack = s.stack[:len(s.stack) - 1]
    }
    if len(s.stack) != 0 {
        ans = s.n - s.stack[len(s.stack) - 1][0]
    } else {
        ans = s.n
    }
    s.stack = append(s.stack, [2]int{s.n, price})
    return ans
}


/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */