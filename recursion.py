'''
a recursive sub routine which is defined in terms of itself
they have a base case - an explicit solution to a recursive function
and a general case - the definition of the recursive function in terms of itself
'''

def stars(n):
    print("*" * n)
    if n > 0 :
        stars(n - 1)

stars(10)

'''
prints: 
**********
*********
********
*******
******
*****
****
***
**
*
'''

def starsTwo(p) :
    if p > 0 :
        starsTwo(p - 1)
    print("*" * p)

starsTwo(4)

'''
prints:
*
**
***
****
'''