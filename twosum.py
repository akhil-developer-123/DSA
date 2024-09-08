class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                currentSum = nums[i] + nums[j]
                if currentSum == target:
                    return [i, j]
