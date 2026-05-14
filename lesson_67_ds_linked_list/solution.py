# Lesson 67: Solution


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, val) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, val) -> None:
        self.head = Node(val, self.head)

    def delete(self, val) -> bool:
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def to_list(self) -> list:
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def reverse(self) -> None:
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def find_middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val if slow else None

    def remove_duplicates(self) -> None:
        seen = set()
        curr = self.head
        prev = None
        while curr:
            if curr.val in seen:
                prev.next = curr.next
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next


ll = LinkedList()
for v in [1, 2, 3, 2, 4, 3, 5]:
    ll.append(v)
print(ll.to_list())           # [1, 2, 3, 2, 4, 3, 5]
ll.remove_duplicates()
print(ll.to_list())           # [1, 2, 3, 4, 5]
print(ll.find_middle())       # 3
ll.reverse()
print(ll.to_list())           # [5, 4, 3, 2, 1]
