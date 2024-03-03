tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

#Aplicando elementos de paso
tag_range = tags [1:-1:2] #Empieza en el 1, temina antes del -1 y se selecciona cada 2 elementos
print(tag_range)

tag_range_two = tags[::2] #Es igual a [0:] --> desde el principio hasta el final, cada dos elementos
print(tag_range_two)

#Invirtiendo el orden de los elementos de la lista
tag_range_three = tags[::-1]
print(tag_range_three)

#La diferencia con sort() es que el criterio de ordenamiento en [::-1] es el index y en .sort(reverse=True) es alfabético
tags.sort(reverse=True)
print(tags)
