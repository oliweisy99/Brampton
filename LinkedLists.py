
class node:
    def __init__(self):
        self.data = None # contains the data
        self.pointer = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None # cur meaning current is set to none

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.pointer = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.pointer



ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()