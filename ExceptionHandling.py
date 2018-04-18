def stuff():
    try:
        number = int(input("enter Number"))
        print(number + 7)
    except:
        print("don't type letters")
        stuff()

stuff()