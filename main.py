def test(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print('*', end='')
            iteration+=1
        print('')
    print('\n When n is',n,'iteration =',iteration)
test(5)
test(10)

print('\n With every n the taken = n**2')
print("(n**2)")