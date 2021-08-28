def fun6():
    i = 65
    for x in range(7):
        for j in range(4):
            print(chr(i), end=' ')
            i += 1
            if i == 91:
                break
        print()

#    i = 65
#    for i in range(7):
#        for j in range(4):
#            print(chr(i), end= '')
#            i+=1
#            if i == 91:
#               break
#       print()
'''
A B C D 
E F G H 
I J K L 
M N O P 
Q R S T 
U V W X 
Y Z 
'''
fun6()