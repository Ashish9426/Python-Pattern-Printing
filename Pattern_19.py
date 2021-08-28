def fun1():
    x = 0
    y = 9
    for i in range(1, 6):
        x = y
        for j in range(1, i+1):
            print(x, end = ' ')
            x = x-1
        print()
        y = y-1

'''
Output : Not Completed
9 
8 7 
7 6 5 
6 5 4 3 
5 4 3 2 1 

'''
# fun1()

def fun2():
    x = 0
    y = 1
    for i in range(1, 6):
        x = y
        for j in range(1, i+1):
            print(x, end = ' ')
            x = x+1
        print()
        y = y+1

'''
Output :
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 

'''
fun2()