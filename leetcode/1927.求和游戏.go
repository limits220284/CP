func sumGame(num string) bool {
    n, sum1, cnt1, sum2, cnt2 := len(num), 0, 0, 0, 0
    for i := 0; i < n/2; i++{
        if num[i] != '?'{
            sum1 += int(num[i] - '0')
        }
        if num[i] == '?'{
            cnt1 += 1
        }
    }
    for i := n/2; i < n; i++{
        if num[i] != '?'{
            sum2 += int(num[i] - '0')
        }
        if num[i] == '?'{
            cnt2 += 1
        }
    }
    if (cnt1 + cnt2) & 1 == 1{
        return true
    }
    return 9 * (cnt1-cnt2) / 2 + sum1-sum2 != 0
}