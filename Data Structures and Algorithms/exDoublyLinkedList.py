class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        node = Node(data, None, self.tail)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def insert_values(self, data_list):
        #self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        current_length = self.get_length()
        if index < 0 or index >= current_length:
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                itr.next.next.prev = node
                return
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                itr.next.next.prev = node
                return
            itr = itr.next

    def remove_at(self, index):
        current_length = self.get_length()
        if index < 0 or index >= current_length:
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        while itr:
            if itr.next is not None:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                    return
            itr = itr.next

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
        itr = self.head
        linked_list_str = ""
        while itr:
            linked_list_str += '[' + str(itr.data) + ']-->'
            itr = itr.next
        print(linked_list_str)

    def print_backward(self):
        if self.tail is None:
            print("Linked list is empty")
        itr = self.tail
        linked_list_str = ""
        while itr:
            linked_list_str += '[' + str(itr.data) + ']-->'
            itr = itr.prev
        print(linked_list_str)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning("lemon")
    ll.insert_at_beginning("cherry")
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("watermelon")
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    print(ll.get_length())
    ll.insert_at(1, "apple")
    ll.print_forward()
    ll.print_backward()
    ll.insert_at(1, "jackfruit")
    ll.print_forward()
    ll.print_backward()
    ll.insert_after_value("jackfruit", "papaya")
    ll.print_forward()
    ll.print_backward()
    ll.remove_at(1)
    ll.print_forward()
    ll.print_backward()
    ll.remove_by_value("jackfruit")
    ll.print_forward()
    ll.print_backward()
    ll.remove_by_value("banana")
    ll.print_forward()
    ll.print_backward()
