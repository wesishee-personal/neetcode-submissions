func hasDuplicate(nums []int) bool {
    m := make(map[int]int)
    for _, num := range nums {
        if _, ok := m[num]; ok {
            // contains dupe so return
            return true
        }
        m[num] = 0
    }
    return false
}
