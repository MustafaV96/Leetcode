class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tempHead = []
        
        while head is not None: 
            tempHead.append(head.val)
            head = head.next
        
        count = 0
        j = len(tempHead)-1
        
        for i in range(0, len(tempHead)):
            if (tempHead[i]==tempHead[j]):
                count = count+1
            j = j-1
                    
        if (count==len(tempHead)):
            return True
        else:
            return False