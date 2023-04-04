class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

    # Insert at the head! aka the beginning of the LinkedList
    def insert(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.next = old_head

    def __str__(self):
        # start with empty string
        text = ""

        # traverse my linked list
        current = self.head     # 1) initialize a variable named current, set to head

        while current: # 2) start while loop, choose between current or current.next
            # 3) Do a thing!
            text += f"{{ {current.value} }} -> "
            current = current.next # 4) move the pointer for current

        return text + "NULL"

    def includes(self, value):
        # traverse my linked list
        current = self.head  # 1) initialize a variable named current, set to head

        while current:  # 2) start while loop, choose between current or current.next
            # 3) Do a thing!
            if current.value == value:
                return True

            current = current.next  # 4) move the pointer for current

        return False


class TargetError:
    pass
