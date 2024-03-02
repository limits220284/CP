func maxLength(arr []string) int {
    ans := 0
    bits := []int{}
    newarr := []string{}
    for _, s := range arr {
        bit := 0
        flag := true
        for _, c := range s {
            c -= 'a'
            if bit & (1 << c) != 0 {
                flag = false
                break
            } else {
                bit |= 1 << c
            }
        }
        if flag {
            bits = append(bits, bit)
            newarr = append(newarr, s)
        }
    }
    n := len(newarr)
    for mask := 1; mask < (1 << n); mask ++ {
        prev := 0
        flag := true
        cnt := 0
        for i := 0; i < 26; i ++ {
            if mask >> i & 1 == 1 {
                if bits[i] & prev == 0 {
                    cnt += len(newarr[i])
                    prev |= bits[i]
                } else {
                    flag = false
                    break
                }
            }
        }
        if flag {
            ans = max(ans, cnt)
        }
    }
    return ans
}