for i in range(2, 10):
    for j in range(2, 10):
        print((str(i) + '*' + str(j) + '=' + str(i * j)).rjust(9), end=' ' * 3)
    print()
