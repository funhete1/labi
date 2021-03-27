counter = 0 
a = int(input("Manda o teu numero ai pai: "))
b = a - 1

for i in range(b, 0, -1):
    c = a % i;
    if(c == 0):
        counter += 1

print("E primo\n") if counter >= 1 else print("Nao e primo\n")