el=[-9,-8,-7,-6,-5,-4,-3.-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]

print(el)

contador1=0
contador2=19
cl=0

while cl<10:
    aux=el[contador1]
    el[contador1]=el[contador2]
    el[contador2]=aux
    contador1=contador1+1
    contador2=contador2-1
    cl=cl+1
    
lista2=[]
for i in range(len(el)):
    lista2.append(el[i])
print (lista2)
