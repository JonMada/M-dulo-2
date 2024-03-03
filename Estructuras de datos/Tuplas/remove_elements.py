post = ('Intro to Python', 'Python basics functions', 'Content')

#Eliminar elementos al final de la tupla: 
post = post[:-1]
print(post)

post = ('Intro to Python', 'Python basics functions', 'Content')

#Eliminar elementos al inicio de la tupla:
post = post[1:]
print(post)

post = ('Intro to Python', 'Python basics functions', 'Content')

#Eliminar elemento específico de la tupla:
post = list(post) #Convertimos nuestra tupla en lista
post.remove('Python basics functions') #Eliminamos el elemento
post = tuple(post) #Lo reconvertimos en tupla
print(post)