class Solution:
    def getIntersectionNode(self,headA,headB):
        #calculate lenghtA
        countA=0
        temp=headA
        while temp:
            countA=countA+1
            temp=temp.next
        #calculate lengthB
        countB=0
        temp=headB
        while temp:
            countB=countB+1
            temp=temp.next
        while(countA>countB):
            headA=headA.next
            countA=countA-1
        while(countB>countA):
            headB=headB.next
            countB=countB-1
        while(headA!=headB):
            headA=headA.next
            headB=headB.next
        return headA
