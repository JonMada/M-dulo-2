#¿Cómo obtener la mediana de una lista con número impar de elementos?
import math

prices = [100,20,3,24,56,76,32,46,65,43,45]
num_of_prices = len(prices) #El objeto prices tiene un número impar de elemento (11)
print(num_of_prices)
prices_sorted = sorted(prices) #Ordenamos los elementos de menor a mayor
print(prices_sorted)

#Dividimos la lista ordenada sabiendo que tenemos un indice de 10
left_side = prices_sorted [:math.floor(num_of_prices/2)] #Math.floor nos devuelve el entero más bajo de la operación (4)
print(left_side)

right_side = prices_sorted [math.ceil(num_of_prices/2):] #Math.ceil nos devuelve el entero más alto de la operación (5)
print(right_side)

median = prices_sorted [math.floor(num_of_prices/2):math.ceil(num_of_prices/2)]
print(median)

