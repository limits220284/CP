func minLength(s string) int {
    stack := make([]byte, 0)
    for i := range s {
        stack = append(stack, s[i])
        m := len(stack)
        if m >= 2 && (string(stack[m - 2:]) == "AB" || string(stack[m - 2:]) == "CD") {
            stack = stack[:m - 2]
        }
    }
    return len(stack)
}