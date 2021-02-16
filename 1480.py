class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solution = []
        sum=0
        for i in range(n):
            sum=sum+nums[i]
            solution.append(sum)
        return solution