func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	seenMap := make(map[byte]int)
	for i:=0; i < len(s); i++ {
		seenMap[s[i]]++
		seenMap[t[i]]--
	}
	for _, v := range seenMap {
		if v != 0 {
			return false
		}
	}
	return true
}
