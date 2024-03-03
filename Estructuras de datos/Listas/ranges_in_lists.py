tags = ['python', 'tutorial', 'development', 'free', 'course']
tag_range = tags[1:2] #El rango se basa en los index, en este caso empieza en 1 y se para antes de llegar al dos
print(tag_range) #Esto nos devuelve un elemento
tag_range_two = tags[1:3] #En este caso empieza en 1 y se para antes de llegar al 3
print(tag_range_two)

#Seleccionar desde un elemento todos los elementos de la lista
tag_range_three = tags[1:] #Dejamos abierto el cierre del rango
print(tag_range_three)

tag_range_four = tags[:2] #Dejamos abierto la apertura del rango
print(tag_range_four)

tag_range_five = tags[:-1] #Seleccionamos todo menos el último elemento (es igual a [0:-1])
print(tag_range_five)

tag_range_six = tags[-2:-1]
print(tag_range_six) #['free']