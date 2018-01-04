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
