from functools import reduce

def manual_exponent (number,exponent):
    return number ** exponent

print(manual_exponent(5,89))

#Aplicando reduce()
def manual_exponent (number, exponent):
    list = [number] * exponent #Aquí se crea la lista de elementos sobre la que se llevará a cabo la iteración 
    return (reduce(lambda total, element: total * element, list)) #Aquí se crea la función lambda que iterará sobre la lista 'list' (total * element + total * element...hasta terminar con los elementos de la lista) 

print(manual_exponent(4,5)) # Es igual a [4,4,4,4,4] --> (((4*4)*4)*4)*4
