class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_len=0
        for i in range(n):
            seen=[]
            for j in range(i,n):
                if s[j] in seen:
                    break
                seen.append(s[j])
                max_len=max(max_len,len(seen))
        return max_len
        