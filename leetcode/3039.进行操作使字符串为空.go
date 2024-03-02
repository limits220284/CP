package main

import (
    "fmt"
    "sort"
)

type pair struct {
    c   rune
    idx int
}

func lastNonEmptyString(s string) string {
    mp := make(map[rune][]int)
    mx := 0
    for i, c := range s {
        t := mp[c]
        mp[c] = append(t, i)
        mx = max(mx, len(mp[c]))
    }
    var arr []pair
    for c, indices := range mp {
        if len(indices) == mx {
            arr = append(arr, pair{
                c:   c,
                idx: indices[len(indices)-1],
            })
        }
    }
    sort.Slice(arr, func(i, j int) bool {
        return arr[i].idx < arr[j].idx
    })

    ans := ""
    for _, p := range arr {
        ans += string(p.c)
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     s := "abracadabra"
//     fmt.Println(lastNonEmptyString(s)) // Output: "ra"
// }
