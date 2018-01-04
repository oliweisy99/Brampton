# Pizza Program
# Oliver Weisfeld
# 4-1-18

Choice = "" #
Again = ""
topCount = 0
index = 0
shopOpen = True
endOrder = False

toppings = [ ("cheese", 10 ), ("Ham", 10), ("Pepperoni", 10), ("Pineapple", 10), ("Mushroom", 10), ("Cherry Tomatoes", 10), ("Chicken", 10), ("Peppers", 10), ("olives", 10), ("Jalapenos", 10) ]

i = 0
n = 0
p = 0
for i in range(10) :
    topping = toppings[i][0]
    StockL = toppings[i][1]
    print(p, " ", topping, " ", StockL)
    p = p + 1


while True:
    base = input("Would you like a (T)hin base or a (P)an base?")
    if base == "P" :
        break
    if base == "p":
        break
    if base == "T" :
        break
    if base == "t" :
        break
    else :
        print("invalid input, try again")
        continue
x = 0
topChoices = [0, 1, 2, 3, 4]
for x in range(4):
    while True:
        tChoice = int(input("select a topping choice from the list [0-9]"))
        if tChoice < 0 :
            print("not valid topping, try again")
            continue
        if tChoice > 9 :
            print("not valid topping, try again")
            continue
        else :
            StockC = toppings[tChoice - 1][1]
            StockC = StockC - 1
            StockC = toppings[tChoice - 1][1]
            if toppings[tChoice - 1][1] >= 1:
                break
            else :
                print(toppings[tChoice - 1][0], " ", "is out of stock")
            break
    topChoices[x] = tChoice
    checker = input("would you like to add another topping? [Y/N]")
    if checker == "Y":
        continue
    else :
        x = 4
        break





'''
class node:
    def __init__(self):
        self.No = None # contains the data
        self.Bs = None # contains the reference to the next node
        self.t = [0, 1, 2, 3, 4]

class linked_list:
    def __init__(self):
        self.cur_node = None # cur meaning current

    def add_node(self, data): # add nodes to linked list
        new_node = node() # create a new node
        new_node.data = data
        new_node.pointer = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node # set the current node to the new one.

    def list_print(self): # prints out nodes
        node = self.cur_node  # cant point to ll!
        while node:
            print(node.data)
            node = node.pointer


ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.list_print()
'''