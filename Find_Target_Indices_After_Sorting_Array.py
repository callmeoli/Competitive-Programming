class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sor = sorted(nums)
        res = [0] * sor.count(target)
        j = 0

        for i in range(0, len(sor)):
            if sor[i] == target:
                res[j] = i
                j += 1
        return res