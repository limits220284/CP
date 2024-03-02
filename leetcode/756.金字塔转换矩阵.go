const m int = 7

func encode(str string) int {
	res, base := 0, 1
	for _, b := range str {
		res += base * int(b-'A')
		base *= m
	}
	return res*10 + len(str)
}

func codeLen(code int) int {
	return code % 10
}

func codeAppend(code int, val int) int {
	l := codeLen(code) + 1
	code /= 10
	pow := codePow(l - 1)
	return (code + val*pow) * 10+l
}

func codePow(pos int) int {
	base := m
	res := 1
	for pos > 0 {
		if pos&1 == 1 {
			res *= base
		}
		pos >>= 1
		base *= base
	}
	return res
}

func decode(code, pos int) int {
	return code / 10 / codePow(pos) % m
}

func pyramidTransition(bottom string, allowed []string) bool {
	allowedMap := make([][]int, m*m)
	for _, str := range allowed {
		key := int(str[0]-'A') + int(str[1]-'A')*m
		allowedMap[key] = append(allowedMap[key], int(str[2]-'A'))
	}
	type void struct{}
	visited := map[int]void{}
	var build func(prevCode int, code int) bool
	build = func(prevCode int, code int) bool {
		if codeLen(prevCode) == 1 {
			return true
		}
		cl := codeLen(code)
		if cl == codeLen(prevCode)-1 {
			if _, ok := visited[code]; ok {
				return false
			}
			visited[code] = void{}
			return build(code, 0)
		}
		key := decode(prevCode, cl) + decode(prevCode, cl+1)*m
		for _, v := range allowedMap[key] {
			if build(prevCode, codeAppend(code, v)) {
				return true
			}
		}
		return false
	}

	return build(encode(bottom), 0)
}