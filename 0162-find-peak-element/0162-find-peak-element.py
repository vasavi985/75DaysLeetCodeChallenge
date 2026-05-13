class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        largest=nums[0]
        index=0
        for i in range(1,len(nums)):
            if nums[i]>largest:
                largest=nums[i]
                index=i
        return index

        