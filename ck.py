for i in range(1000):
    # print((pow(i, 2) % 13) )

    if ( (2**i) % 13) == 6 :
        print(i)
        break