class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            i=len(str(i))
            if i%2==0:
                count+=1
        return count

        