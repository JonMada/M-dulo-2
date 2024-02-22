#Tomar el valor absoluto
loss = -20.25
print(abs(loss)) #Nos devuelve 20.25

#Redondear al valor más bajo
import math
product_cost = 89.99
print(math.floor(product_cost)) #Nos devuelve el valor redondeado al entero más bajo

#Redondear al valor entero más alto 
import math
product_cost = 89.99
print(math.ceil(product_cost))

#Combinación de funciones (abs + floor)
import math
loss = -20.25
print(abs(math.floor(loss))) #Nos devuelve 21 porque al ser un número negativo el floor está en 21, es menor (el ceil en 20)

#Redondeo de toda la vida
product_cost = 89.02
product_cost_two = 89.56
print(round(product_cost)) #Resultado: 89
print(round(product_cost_two)) #Resultado: 90

#Raíz cuadrada
import math
product_cost = 89.12
print(math.sqrt(product_cost)) #Resultado: 9.440338976
print(math.ceil(math.sqrt(product_cost))) #Si quisiesemos redondearlo al entero más alto
print(round(math.sqrt(product_cost))) #Si quisiesemos simplemente redondearlo

#Exponentes 
import math
product_cost = 89.12
print(math.pow(product_cost,2)) #Resultado: 7942.374400000001 --> ques es lo mismo que 89.12**2, por eso coje dos argumentos 