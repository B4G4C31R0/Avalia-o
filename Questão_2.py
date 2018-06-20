lista2=[90,2,3,4,5,6,7,73,9,10,11,12,13,141,15,16,170,18,19,20,211,22,23,24,25]
print(lista2)

#Maior e menor
menor=90
maior=90
for i in range(len(lista2)):
    if lista2[i]>maior:
        maior=lista2[i]
    elif lista2[i]<menor:
        menor=lista2[i]

for i in range(len(lista2)):
    if lista2[i]==maior:
        print ("Maior número: {}".format(lista2[i]))
        print ("Índice do maior número: [{}]".format(i))
for i in range(len(lista2)):
    if lista2[i]==menor:
        print ("Menor número: {}".format(lista2[i]))
        print ("Índice do menor número: [{}]".format(i))

#Media        
def media(lista2):
    soma=0
    for i in lista2:
        soma=i+soma
        m=soma/len(lista2)
    return m
print ("A média é: {}".format(media(lista2)))

pad=0
for x in lista2:
    p=(x-media(lista2))**2
    pad+=p/(len(lista2)-1)
print(pad**0.5)
