def fun6():
    i = 65
    for x in range(7):

        for j in range(4):
            print(chr(i), end=' ')
            i += 1
            if i == 91:
                break
        print()
'''
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
fun6()
