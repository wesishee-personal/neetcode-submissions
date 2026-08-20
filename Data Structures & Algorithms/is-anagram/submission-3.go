func isAnagram(s string, t string) bool {
	setS := make(map[rune]int)
	setT := make(map[rune]int)

	if len(s) != len(t){
		return false
	}
	for i, r := range s {
		setS[r]++
		setT[rune(t[i])]++
	}
	for k, v := range setS {
		if setT[k] != v {
			return false
		}
	}
	return true

}
