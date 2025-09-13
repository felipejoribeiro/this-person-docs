from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # string representation of the linked list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


class Solution:
    def appendToLList(self, LList, value):
        if LList.val is None or LList.val == 0:
            LList.val = value
            return LList
        else:
            LList.next = ListNode(
                val=value,
                next=None,
            )
        return LList.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None or list1.val is None:
            return list2
        elif list2 is None or list2.val is None:
            return list1

        response = ListNode()
        cursor = response
        while True:
            if list1 is None and list2 is None:
                return response
            elif list1 is None:
                cursor = self.appendToLList(cursor, list2.val)
                list2 = list2.next
            elif list2 is None:
                cursor = self.appendToLList(cursor, list1.val)
                list1 = list1.next
            elif list1.val >= list2.val:
                cursor = self.appendToLList(cursor, list2.val)
                list2 = list2.next
            else:
                cursor = self.appendToLList(cursor, list1.val)
                list1 = list1.next


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(None)
    l2 = ListNode(None)
    merged = sol.mergeTwoLists(l1, l2)
    print(merged)
