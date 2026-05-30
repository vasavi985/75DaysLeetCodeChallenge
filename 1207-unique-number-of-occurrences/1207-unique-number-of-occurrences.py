class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}
        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        seen={}
        for i in count:
            if count[i] in seen:
                return False
            else:
                seen[count[i]]=1
        return True
            