class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        temp=[]
        for i in range(len(nums)):
            total+=nums[i]
            temp.append(total)
        return temp


        