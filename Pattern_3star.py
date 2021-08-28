def fun3():
    for x in range(1, 10, 2):
        for y in range(1, x+1):
            print("*", end = ' ')
        print()

'''
Output :
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * *
'''

fun3()