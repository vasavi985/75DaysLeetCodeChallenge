class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        nums.sort()
        freq_list = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                freq_list.append((nums[i-1], count))
                count = 1  # Reset count for new element
        freq_list.append((nums[-1], count)) # Handle last group
        
        # Sort by frequency descending
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in freq_list[:k]]