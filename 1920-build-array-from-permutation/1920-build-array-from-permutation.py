class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            i=nums[nums[i]]
            result.append(i)
        return result
        