#Ejemplo tuple
post = ('Intro to Python', 'Python basics functions', 'Content')
post_list = ['Intro to Python', 'Python basics functions', 'Content']

#### Es immutable
# post[1] = 'A'  #TypeError

post_list[1] = 'A' #Las listas si son mutables
print(post_list)

#Seleccionar elementos
# heading = post[0]
# subheading = post[1]
# content = post[2]

# print(heading)
# print(subheading)
# print(content)

#Otras técnica de selección para 'desempaquetar'
heading, subheading, content = post 

print(heading)
print(subheading)
print(content)