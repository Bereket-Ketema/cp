class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l,r=0,0
        num3=[]
        while l<m and r<n:
            if nums1[l]<=nums2[r]:
                num3.append(nums1[l])
                l+=1
            else:
                num3.append(nums2[r])
                r+=1
        num3.extend(nums1[l:m])
        num3.extend(nums2[r:])
        nums1[:m+n] = num3