class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num in nums1:
            index = nums2.index(num)   # find element position in nums2
            found = -1

            # search on right side
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    found = nums2[i]
                    break

            result.append(found)

        return result