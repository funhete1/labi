import random

counter, num = 0, 0
r = random.randint(0,100)     
print(r)
while True:      
    num = int(input("Diz um numero ai: "))
    print("Mais baixo") if num > r else print("Mais alto")
    counter += 1       
    if(num == r):
        print("Parabens o burro so te custaram "+  str(counter) + " tentativas\n")
        break