class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            i=nums[nums[i]]
            ans.append(i)
        return ans