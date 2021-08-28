def fun13():
    i = j = 1
    space = 5
    for x in range(5):

        for y in range(space):
            print(end= ' ')
        print(i)
        j=j*10+1
        i=j*j
        space-=1 # space = space -1
'''
not solved !
solve it !

     1
    121
   12321
  1234321
 123454321
  1234321
   12321
    121
     1
'''
fun13()