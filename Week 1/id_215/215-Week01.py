# leet code #26

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # First, I think we can just list(set(num)) to get the result 
        # but the type erro occurs, seems like we cannot use the set() function 
        # Scond, I conder about using the pointer to get the result
        # we set i as pointer and move to the end when the value of the next elment 
        # is the same to the previous element, then we delete it
        # The time complexity is O(n) because of one loop
        i = 0
        while i < len(nums): # the pionter
            if nums[i]==nums[i-1]:
                del(nums[i])
            else:
                i+=1
        return i
    
    # Another solution (from discussion):
    # set two pointers i nad j, the pionter i store the unduplicated result 
    # let the pionter j move around
    # def (self, nums：list[int])->int:
    #   i,j=1,1  # set two pointers
    #   while j < len (nums):  
    #       if nums[i-1]!=nums[j]:
    #           nums[i]=nums[j] #  # the pionter move from i to j under this condition
    #           i+=1 # the pinter i go to next 
    #       j+=1  # move j under while condition 
    #   return i
    
    
# leet code #21 


class Solution:
# these two are linked lists not array and they are not iterable
# so we cannot use the for loop and we have to get the value by using .next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # the edge cases:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        elif l1.val <l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2) # recursively merge
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)

    def mergeTwoLists2 (self, l1: ListNode, l2: ListNode) ->ListNode:
        # set a reference of the node which will not change named prev 
        prev = ListNode(0)
        head = prev
        
        while l1 and l2:
            if l1.val<=l2.val:
                head.next=l1 # the next node of head is node in l1
                l1 = l1.next
            else:
                head.next=l2 # the next node is node in l2
                l2= l2.next
            
            head = head.next  # append node and move to next

        if l1 is None and l2 is not None:
            head.next = l2
        elif l1 is not None and l2 is None:
            head.next = l1

        # return the nodes 
        return prev.next  # if we return 'head' it will be [4,4] 