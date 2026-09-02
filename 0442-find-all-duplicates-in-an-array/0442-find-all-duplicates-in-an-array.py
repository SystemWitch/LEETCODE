class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict={}
        x=[]
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in dict:
            if dict[i]>1:
                x.append(i)

        return x