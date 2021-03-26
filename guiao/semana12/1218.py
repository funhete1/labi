carry = 1

num = int(input("Manda um numero ai pai: "))
if num < 0:
    print("Mas tu e burro ou oq ?")
    exit

else:
    num_ = num

    while num > 1:
        carry = carry * num
        num = num - 1

    print(str(num_) + "! = " + str(carry))
    


