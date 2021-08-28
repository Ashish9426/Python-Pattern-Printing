def fun8():
    for x in range(5, 0, -1):
        for y in range(1, x+1):
            print(x, end = ' ')
        print()


'''
Output :
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1  
'''

# fun8()

def fun():
    for x in range(5, 0, -1):
        for y in range(x):
            print(x, end = ' ')
        print()

fun()