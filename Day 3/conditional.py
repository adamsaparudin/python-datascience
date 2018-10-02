while True:
    numb1 = int(input("Input bilangan bulat 1: "))
    numb2 = int(input("Input bilangan bulat 2: "))
    if (numb1 > numb2):
        print("{} lebih besar dari pada {}".format(numb1, numb2))
    elif (numb1 == numb2):
        print("{} bernilai sama dengan {}".format(numb1, numb2))
        # print(str(numb1) + " bernilai sama dengan " + str(numb2))
        # jika tidak menggunakan method str maka akan error.
    else:
        print("{} kurang dari {}".format(numb1, numb2))


