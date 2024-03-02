func maximumUnits(boxTypes [][]int, t int) int {
    // sort
    sort.Slice(boxTypes, func(i, j int) bool {
        return boxTypes[i][1] >= boxTypes[j][1]
    })
    fmt.Println(boxTypes)
    ans := 0
    for _, x := range boxTypes {
        if x[0] < t {
            ans += x[1] * x[0]
            t -= x[0]
        } else {
            ans += t * x[1]
            break
        }
    }
    return ans
}