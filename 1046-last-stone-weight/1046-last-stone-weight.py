class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()

            x = stones.pop()   # biggest
            y = stones.pop()   # second biggest

            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0