names = ['Jon', 'Ane', 'Valeria', 'Kel', 'Miren', 'Patxi', 'Bruce']
print(names)

#Sort function
names.sort() #Nos ordena la lista por orden alfabético
print(names)

#Si queremos ordenarlos al reves Z-A
names.sort(reverse=True)
print(names)

#Sorted function: en vez de efectuar cambios sobre el objeto los asocia a uno nuevo
names = ['Jon', 'Ane', 'Valeria', 'Kel', 'Miren', 'Patxi', 'Bruce']
names_new_az_order = sorted(names)
print(names_new_az_order)

#Si queremos ordenarlos al reves Z-A
names_new_za_order = sorted(names,reverse=True)
print(names_new_za_order)

