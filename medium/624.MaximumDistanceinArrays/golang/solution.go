func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func maxDistance(arrays [][]int) int {
	max_ele, min_ele := arrays[0][len(arrays[0])-1], arrays[0][0]
	distance := 0
	for index, arr := range arrays {
		if index == 0 {
			continue
		}
		distance = max(
			max(abs(max_ele-arr[0]),
				abs(arr[len(arr)-1]-min_ele),
			),
			distance,
		)
		max_ele = max(arr[len(arr)-1], max_ele)
		min_ele = min(arr[0], min_ele)
	}
	return distance
}