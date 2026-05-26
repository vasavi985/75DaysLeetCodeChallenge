class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        for i in sentences:
            count=0
            for word in i:
                if word==" ":
                    count+=1
                if count>maximum:
                    maximum=count
        return maximum+1
        