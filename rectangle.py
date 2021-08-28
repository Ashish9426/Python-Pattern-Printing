size = int(input('Enter no: '))

for i in range(1, size+1):
    for j in range(1, size+1):
        if i==1 or i==size:
            print("*", end = ' ')
        else:
            if j==1 or j==size:
                print("*", end = ' ')
            else:
                print(" ", end = ' ')
    print()

# '''
# size = int(input('Enter no: '))
#
# for i in range(1, size+1):
#     for j in range(1, size+1):
#         if i==1 or i==size:
#             print("*", end = ' ')
#         else:
#             if j==1 or j==3 or j==size:
#                 print("*", end = ' ')
#             else:
#                 print(" ", end = ' ')
#     print()
#
#
#
# '''
# def out():
#
# '''
# * * * * *
# *   *   *
# *   *   *
# *   *   *
# * * * * *
# '''
#
#
# out()

