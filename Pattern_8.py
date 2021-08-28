def fun8():
    for x in range(5, 0, -1):
        for y in range(1, x+1):
            print(y, end = ' ')
        print()

'''
Output :
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

fun8()