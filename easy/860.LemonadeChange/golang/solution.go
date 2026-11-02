func lemonadeChange(bills []int) bool {
	five, ten := 0, 0
	for _, item := range bills {
		switch item {
		case 5:
			five++
		case 10:
			ten++
			if five == 0 {
				return false
			}
			five--
		case 20:
			if ten < 1 && five < 3 || ten >= 1 && five == 0{ // less than 15
				return false
			} else if ten == 0 {
				five -= 3
			} else {
				ten--
				five--
			}
		}
	}
	return true
}