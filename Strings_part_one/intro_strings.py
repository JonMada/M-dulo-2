#Uso de las comillas y problemas frecuentes

sentence = 'The quick brown fox jumped over the lazy dog'
sentence_two = 'That is my dog\'s bowl' #Resolvemos el problema con \ para que considere ' como parte del str.
sentence_three = "That is my dog's bowl"
sentence_four = "Tiffany said, \"That is my dog's bowl\""

print(sentence_four)


#Flujo de trabajo de los procesos 

#1) El string se transformará a mayúsculas
sentence = 'The quick fox jumped'.upper()
print(sentence)

#2) El string se transformará a mayúsculas pero ese proceso no se almacena, por lo que no habrá modificación real.
sentence = 'The quick fox jumped'
sentence.upper()
print(sentence)

#3) El string se transformará a mayúsculas y ese proceso se almacena en otra variable para no modificar la original
sentence = 'The quick fox jumped'
sentence_upper = sentence.upper()

print(sentence)
print(sentence_upper)

#4)Transformar la primera letra del string a mayúscula
sentence = 'the quick fox jumped'.capitalize()
print(sentence)

#5)Transformar la primera letra de todas las palabras  del string a mayúscula
sentence = 'the quick fox jumped'.title()
print(sentence)

#6)Transformar el string de mayúsculas a minúsculas
sentence ='THE QUICK FOX JUMPED'.lower()
print(sentence)

### Cómo extraer subcadenas de un string ###

# Indice del string
# T -> 0
# h -> 1
# e -> 2
# ' ' -> 3

starter_sentence = 'The qick brown fox jumped'
first_word = starter_sentence[0:3]
new_sentence = first_word
print(new_sentence)

#Modificar un string

second_sentence = "The quick black fox jumped"
second_new_sentence = 'Thy' + second_sentence[3:] #Si no indicamos un valor final en el rango Python entenderá que lo seleccionamos hasta el final

print(second_new_sentence)