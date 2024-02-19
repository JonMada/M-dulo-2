url = 'https://google.com'

#Función strip ()
print(url.strip()) #Elimina los espacios extra al principio y al final
print(url.strip('https://')) #Elimina la substring que indiquemos

#Función lstrip() --> elimina los caracteres del principio de la cadena
print(url.lstrip('https://'))

#Función rstrip() --> elimina los caracteres del final de la cadena
print(url.rstrip('.com'))
                 

#Ejercicio: de https://google.com a Google

url = 'https://google.com'
url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)