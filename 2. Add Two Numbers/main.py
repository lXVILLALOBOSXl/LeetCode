# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0  # Initialize the carry to 0
        dummy = ListNode(0)  # Dummy node to start the result list
        current = dummy  # Pointer to track the current node in the result
        
        # Loop until both l1 and l2 are exhausted and there's no carry
        while l1 or l2 or carry:
            # Get the values from l1 and l2, or 0 if one of them is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the two digits and the carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10  # Update the carry (1 if total_sum >= 10, otherwise 0)
            new_val = total_sum % 10  # The new digit to store in the current node
            
            # Create a new node with the calculated digit and move the current pointer
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
        
        

# Test cases
s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
# 807


result = s.addTwoNumbers(l1, l2)
string = "["
while result.next is not None:
    string += str(result.val) + ", "
    result = result.next
string += str(result.val)
string += "]"

print(string)