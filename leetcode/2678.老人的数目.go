func countSeniors(details []string) int {
    ans := 0
    for i := 0; i < len(details); i++{
        age, _ := strconv.Atoi(details[i][11:13])
        if(age > 60) {
            ans += 1
        }
    }
    return ans
}