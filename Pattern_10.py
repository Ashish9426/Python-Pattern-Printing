def fun10():
    i = j = 1
    for x in range(5):
        print(i)
        j = j*10+1
        i = j*j

'''
Output :
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1  
'''

fun10()