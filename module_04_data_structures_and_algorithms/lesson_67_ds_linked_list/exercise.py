# Lesson 67: Exercise — Linked Lists


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # TODO: append(val) — add to end
    # TODO: prepend(val) — add to front
    # TODO: delete(val) — remove first occurrence, return True if found
    # TODO: to_list() -> list — return all values as a list

    # TODO: reverse() — in-place, no return value

    # TODO: find_middle() -> val — use slow/fast pointer technique
    #   For even-length list, return the SECOND middle node

    # TODO: remove_duplicates() — keep first occurrence of each value


# Test
# ll = LinkedList()
# for v in [1, 2, 3, 2, 4, 3, 5]:
#     ll.append(v)
# print(ll.to_list())            # [1, 2, 3, 2, 4, 3, 5]
# ll.remove_duplicates()
# print(ll.to_list())            # [1, 2, 3, 4, 5]
# print(ll.find_middle())        # 3
# ll.reverse()
# print(ll.to_list())            # [5, 4, 3, 2, 1]
