class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        result = []

        first = nums[:n]
        second = nums[n:]

        for i in range(n):
            result.append(first[i])
            result.append(second[i])

        return result