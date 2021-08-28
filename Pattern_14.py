def fun14():
    i = 0
    for x in range(1,6):
        for y in range(4):
            if x%2 == 0:
                print('0', end= '')
            else:
                print('1', end= '')
        print()
'''
1111
0000
1111
0000
1111
'''
fun14()