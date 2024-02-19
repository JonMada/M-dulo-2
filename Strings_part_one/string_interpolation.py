name = 'Valeria'
saludo = f'Hola {name}'
print(saludo) 

#Si nuestro string contiene corchetes

name = 'Valeria'
saludo = f'Este es el blog de {name} sobre los {{corchetes}} y Python'
print(saludo)

#Si estamos trabajando con string multilinea (heredocs)

name = 'Valeria'
apellido = 'Madariaga'
product = 'Curso de inglés'
email_content = f'''
Hola {name} {apellido}.
Gracias por la compra de su {product}
Atentamente,
Equipo de ventas
'''
print(email_content)

#Format method --> es un método utilizado hace tiempo, algo desactualizado

name = 'Valeria'
apellido = 'Madariaga'
product = 'Curso de inglés'
email_content = '''
Hola {0} {1}.
Gracias por la compra de su {2}
Atentamente,
Equipo de ventas
'''.format(name,apellido,product) #Los número representan el índice de los parámetros de la función.

print(email_content)

