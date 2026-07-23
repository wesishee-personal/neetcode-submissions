class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let numsMap = new Map();
        for (let j = 0; j < nums.length; j++) {
            let otherVal = target - nums[j];
            if (numsMap.has(otherVal)) {
            console.log("otherVal = "+numsMap.get(otherVal));
            console.log("nums[j] = "+nums[j]);
            return [numsMap.get(otherVal), j];
            }
            numsMap.set(nums[j], j);
        }
        return [];

    }
}
