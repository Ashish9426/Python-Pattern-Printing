def fun2():
    for x in range(5, 0, -1):
        for y in range(1, x+1):
            print("*", end = ' ')
        print()

'''
Output :
* * * * * 
* * * * 
* * * 
* * 
* 
'''

fun2()