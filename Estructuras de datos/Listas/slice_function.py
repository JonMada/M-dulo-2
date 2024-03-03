tags = ['python', 'development', 'tutorial', 'code', 'programming']
print(tags[:2]) #Método clásico de rangos

#Slice function
sliced_tag = slice(2) #Nos permite almacenar nuestro método en un objeto
print(sliced_tag) #slice(None, 2, None) --> Características de nuestro slice(star, stop, step)
print(tags[sliced_tag]) #Aplicamos a nuestra lista las características de nuestro slice

slice_tag_two = slice(1,4,2)
print(tags[slice_tag_two])
print(tags[1:4:2]) #Funciona igual que los rangos

#Para conocer las características de nuestro slice (start, stop, step)
print(slice_tag_two.start)
print(slice_tag_two.stop)
print(slice_tag_two.step)