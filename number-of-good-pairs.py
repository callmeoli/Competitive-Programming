class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        for i in range (0, len(nums)):
            for j in range (0, len(nums)):
                if i != j and nums[i] == nums[j]:
                    good += 1
        good = good // 2
        return (good)
