import operator
from functools import reduce

'''
Tenemos que construir una función que sume, reste, multiplique
y divida los elementos de la matriz de manera automática

dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '-') # -
dynamic_reducer([1, 2, 3], '*') # 6
dynamic_reducer([1, 2, 3], '/') # -
'''

def dynamic_reducer (collection, op):
    operators = {
        '+': operator.add,
        "-": operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    return reduce((lambda total, element:operators [op](total, element)), collection)

print(dynamic_reducer([1,34,5], '/'))
print(dynamic_reducer([1,34,5], '*'))
print(dynamic_reducer([1,34,5], '+'))
print(dynamic_reducer([1,34,5], '-'))
