class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict={}
        x=[]
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        m=len(nums)
        for i in range(1,m+1):
            if i not in dict:
                x.append(i)
        return x

