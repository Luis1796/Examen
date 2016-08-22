import zipper
n = int(input("Ingresa longitud listas "))

lista1=[]
lista2=[]
print("Datos lista1")
for i in range(0,n): 
	lista1.append(int(input("Enteros "))) 

print("Datos lista2")
for i in range(0,n): 
	lista2.append(input("Cadena ")) 
print(lista1)
print(lista2)

listaZ=zipper.zip(lista1,lista2)  
print(listaZ)
listau1,listau2=zipper.unzip(listaZ)
print(listau1)
print(listau2)


