func grayCode(n int) []int {
    power := 1 << n
	result:= make([]int, 0, power)
	for i := 0; i < power; i++ {
		result = append(result, i ^ (i >> 1))
	}
	return result
}
