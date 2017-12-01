def prime():
    n = int(input("Num: "))
    if n == 0:
        print("Not Prime")
    elif n == 1 or n == 2:
        print("Prime")
    
    if all(n%x != 0 for x in range(2,n)):
        print("Prime")
    else:
        print("Not Prime")
    prime()



prime()
