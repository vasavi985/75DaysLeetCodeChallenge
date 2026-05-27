class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            if i%2==0:
                result.append(i)
        for j in nums:
            if j%2!=0:
                result.append(j)
        return result
        