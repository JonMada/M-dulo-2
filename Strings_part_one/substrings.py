sentence = "The quick brown fox jumped over the lazy dog"

#Find method
query = sentence.find('quick')
print(query)
'''
Si buscamos una substring que no se encuentre
en la cadena de texto, esta función nos devolverá
-1.
'''

#Index method
query = sentence.index('quick')
print(query)
'''
Si buscamos una substring que no se encuentre
en la cadena de texto, esta función nos devolverá
ERROR.
'''

#In operator (la más utilizada)
query = 'fox' in sentence
print(query)