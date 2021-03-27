soma, media, counter = 0, 0, 0 
num = []
while True:
    a = int(input("Numero: "))
    num.append(a)
    if(num[counter] == 0):break
    counter+=1
        
for i in range(0, len(num)):
    soma = soma + num[i]
    if(num[0] == 0):
        break
    media = soma / counter
    
print(" soma: " +str(soma)+ "\n media: " +str(media)+ "\n lista: " +str(num))