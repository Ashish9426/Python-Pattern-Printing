def fun12():
    for i in range(6):
        for j in range(10):
            if j>=6-i and j<=4+i:
                print("*", end= '')
            else:
                print()
        print()

fun12()