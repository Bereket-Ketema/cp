class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        store={}
        for value in nums:
            store[value] = store.get(value,0)+1
        return(max(store, key=store.get))