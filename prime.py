def prime():
    n = int(input("Num: "))

    if all(n%x != 0 for x in range(2,n)):
        print("True")
    else:
        print("False")
    prime()



prime()
