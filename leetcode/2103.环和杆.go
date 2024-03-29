var POLE_NUM, COLOR_NUM = 10, 3
func countPoints(rings string) int {
    state := make([][]int, POLE_NUM)
    for i := 0; i < POLE_NUM; i++ {
        state[i] = make([]int, COLOR_NUM)
    }
    n := len(rings)
    for i := 0; i < n; i += 2 {
        color := rings[i]
        pole_index := rings[i + 1] - '0'
        state[pole_index][getColorId(color)] = 1
    }
    res := 0
    for i := 0; i < POLE_NUM; i++ {
        flag := true
        for j := 0; j < COLOR_NUM; j++ {
            if state[i][j] == 0 {
                flag = false
                break
            }
        }
        if flag {
            res += 1
        }
    }
    return res
}

func getColorId(color byte) int {
    if color == 'R' {
        return 0
    } else if color == 'G' {
        return 1
    }
    return 2
}