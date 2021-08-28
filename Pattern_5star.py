# 1st Method
def fun4():
    for x in range(1, 10, 2):
      print('*' *x)

# 2nd Method
def fun4_1():
    for x in range(1, 10, 2):
        for y in range(1, x+1):
            print("*", end = ' ')
        print()

'''
Output :
*
***
*****
*******
*********
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * * 
'''

fun4()
fun4_1()