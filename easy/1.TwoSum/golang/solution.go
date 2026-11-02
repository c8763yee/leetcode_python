func twoSum(nums []int, target int) []int {
    maps := map[int]int{}
    for index, num:= range nums{
        
        if diff, exists := maps[target-num]; exists == true{
            return append(make([]int, 0, 2), index, diff)
        }else{
            maps[num] = index
        }
            
    }
    return []int{}
}