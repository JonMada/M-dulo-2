#Trabajando con números tipo float

product_cost = 88.40
commision_rate = 0.08
quantity_items_sold = 450

product_cost += (commision_rate * product_cost) #Aqui calculamos el costo total de la unidad de producto con la comisión de venta
print(product_cost * quantity_items_sold) #El costo total contabilizando cada item que se ha vendido = 42962.4

#Trabajando con números tipo decimal

from decimal import Decimal #Aquí estamos importando la libería decimal de Python y la clase Decimal de esa librería (hay que hacerlo de manera expresa)

product_cost = Decimal(88.40) #De este modo aplicamos la función que convierte el float en decimal
commision_rate = Decimal (0.08)
quantity_items_sold = Decimal(450)

product_cost += (commision_rate * product_cost)
print(product_cost * quantity_items_sold) # Resultado 42962.40000000000282883716451

