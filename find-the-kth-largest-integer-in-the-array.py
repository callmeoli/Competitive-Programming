class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort()
        number=[]
        for i in nums:
            number.append(eval(i))
        number.sort()
        print(number)
        result = str(number[len(nums) - k])
        return result
