class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new=nums1+nums2
        new.sort()
        total_l=len(new)
        i=total_l//2
        if total_l%2!=0:
            return new[i]
        else:
            return (new[i-1]+new[i])/2
            