post = ('Intro to Python', 'Python basics functions', 'Some cool content')
print(id(post)) #Nos da el id de este objeto

#Aqui estamos no estamos editando la tupla inicial, simplemente renombramos la tupla con el mismo nombre (sobreescribimos)
# post = post + ('published',) #La coma sirve para que Python interprete que es un tupla, si no la ponemos entenderá que es un str y no se podrá añadir

post += ('published',) #Representa lo mismo que arriba
print(id(post)) #Nos da el id de este objeto, vemos que no es el mismo que el primer 'post' ya que es otro objeto sobreescrito.


print(post) #Vemos que se ha añadidos correctamente

title, subtitle, content, status = post

print(title)
print(subtitle)
print(content)
print(status)