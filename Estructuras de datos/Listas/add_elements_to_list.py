tags = ['tutorial', 'development', 'code', 'tutorials']

#Extend() function --> modifica la lista original

tags.extend('Programming') #Incluirá cada caracter como elemento de la lista
print(tags)

tags.extend(['Programming']) #Lo incluirá como un elemento de la lista
print(tags)

#Más ejemplos
prices = [1,2,3,45,5,6,4,2323,23]
prices_two = [3,4,523,5,4,2,1,3]

prices.extend(prices_two)
print(prices)

#Alternativa para no modificar la lista original
tags_two = ['tutorial', 'development', 'code', 'tutorials']
new_tags = tags_two + ['Programming']
print(tags_two)
print(new_tags)

#Más ejemplos
prices = [1,2,3,45,5,6,4,2323,23]
prices_two = [3,4,523,5,4,2,1,3]
all_prices = prices + prices_two
print(prices)
print(prices_two)
print(all_prices)