func hasDuplicate(nums []int) bool {
    merp := make(map[int]int)
    for i:=0; i < len(nums); i++ {
        if _, ok := merp[nums[i]]; ok {
            return true
        }
        merp[nums[i]] = 1
    }
    return false
}
