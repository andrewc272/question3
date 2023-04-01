import delete_operation_singly_linkedlist as linkedList

class queue:
    def __init__(self):
        self.list = linkedList.SinglyLinkedList()

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        first = self.first()
        self.list.delete_first_node()
        return first
        
    def first(self):
        return self.list.head.data
