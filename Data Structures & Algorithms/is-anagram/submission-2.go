func isAnagram(s string, t string) bool {
	set := make(map[rune]int)
	if len(s) != len(t){
		return false
	}
	for _, r := range s {
		set[r]++
	}
	for _, r := range t {
		if _, ok := set[r]; ok {
			set[r]--
			if set[r] == 0 {
				delete(set, r)
			}
		} else {
			return false
		}
	}
	return len(set) == 0

}
