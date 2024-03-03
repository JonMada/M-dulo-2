#join() --> nos permite conectar elementos de una cadena, especificando un separtador
#¡¡¡Sólo puede ser utilizada en listas que contengan elementos tipo string!!!

lista_palabras = ['Hola', 'cómo', 'estás']
cadena_resultante = " ".join(lista_palabras) #Secuencia: especificamos separador y la lista a la que aplicamos la función
print(cadena_resultante)

#Ejercicio práctico con join()
#https://www.google.com/search?q=python+devolpment+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python','devolpment','tutorial']
formatted_tags = "+".join(tags)
query_uri = f'{uri}{formatted_tags}' #Aquí aplicamos la sintáxis para la interpolación de cadenas
print(query_uri)
