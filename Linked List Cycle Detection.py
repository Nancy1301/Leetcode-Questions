# Linked List Cycle Detection

# TWO WAYS:

# 1st - time complexity as O(n) and space complexity as O(n):

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False


# 2nd - time complexity as O(n) and space complexity as O(1):

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
