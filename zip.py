def zip(lista1,lista2):

	j=0 
	tupla =[]

	for  i in lista1:  
		tupla.append([(i,lista2[j])]) 
		j+=1
	print(tupla) 


