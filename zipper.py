def zip(lista1,lista2):

	j=0 
	tupla =[]

	for  i in lista1:  
		tupla.append([(i,lista2[j])]) 
		j+=1
	print(tupla) 


def unzip(lista):
	lista1=[]
	lista2=[]
	for i in range(0,len(lista)):
		lista1.append(lista[i][0])
		lista2.append(lista[i][1])
	return lista1, lista2