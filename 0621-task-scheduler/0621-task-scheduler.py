from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxFreq = max(freq.values())

        maxCount = 0
        for value in freq.values():
            if value == maxFreq:
                maxCount += 1

        result = (maxFreq - 1) * (n + 1) + maxCount

        return max(result, len(tasks))