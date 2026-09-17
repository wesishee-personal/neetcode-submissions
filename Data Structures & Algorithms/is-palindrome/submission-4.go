func isPalindrome(s string) bool {
	runes := []rune(s)
	j := len(runes)-1
	i := 0
	for i < j {
		if !(unicode.IsLetter(runes[i]) || unicode.IsDigit(runes[i])) {
			i++
			continue
		}
		if !(unicode.IsLetter(runes[j]) || unicode.IsDigit(runes[j])) {
			j--
			continue
		}
		if unicode.ToLower(runes[i]) != unicode.ToLower(runes[j]) {
			fmt.Printf("i = %c, j = %c", runes[i], runes[j])
			return false
		}
		i++
		j--
	}
	return true
}
