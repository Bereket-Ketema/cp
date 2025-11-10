class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l,r=0,0
        result=[]
        nums1.sort()
        nums2.sort()
        while l < len(nums1) and r < len(nums2):
            if nums1[l]==nums2[r]:
                result.append(nums1[l])
                l+=1;r+=1
            elif nums1[l]<nums2[r]:
                l+=1
            else:
                r+=1
        return result
