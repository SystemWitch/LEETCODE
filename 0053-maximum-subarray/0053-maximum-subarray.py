class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x=0
        maxi=float('-inf')
        for i in range(len(nums)):
            if len(nums)==1:
                return nums[i]
            if x<0:
                x=0
            x+=nums[i]
            maxi=max(x,maxi)
        return maxi
