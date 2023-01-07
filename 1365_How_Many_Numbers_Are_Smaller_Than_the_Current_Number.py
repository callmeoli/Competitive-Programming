class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        new = [0] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                num2 = nums[i]
                if num2 > nums[j]:
                    new[i]= new[i] + 1
        return new
