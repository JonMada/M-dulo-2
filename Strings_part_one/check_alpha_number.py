api_data = '5'
greeting = 'Hi'
greeting_two = 'Hi there'


print(api_data.isalpha())
print(greeting.isalpha())
print(greeting_two.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())
print(greeting_two.isnumeric()) #Si el string no contiene el 100% de caracteres alfanumericos, devolverá false (el espacio no se considera alfanumeric)