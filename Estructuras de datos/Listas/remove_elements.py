users = ['Ane','Valeria', 'Ane', 'Jon', 'Bruce','Jon']

#Función remove()
users.remove('Ane') #Remove() toma como valor el elemento que queremos eliminar y elimina el primer elemento coincidente
print(users)

#Función pop()
popped_user = users.pop() #Expulsa el último elemento de la lista y lo almacena
print(popped_user)
print(users)

#Delete command
del users[0] #Borra el elemento que indiquemos de la lista a través del index
print(users)