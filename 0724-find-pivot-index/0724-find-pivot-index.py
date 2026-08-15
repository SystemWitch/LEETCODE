class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        n=len(nums)
        total=sum(nums)
        for i in range(n):
            rightsum=total-nums[i]-leftsum
            if rightsum==leftsum:
                return i
            leftsum+=nums[i]
        return -1