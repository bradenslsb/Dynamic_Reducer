import operator
from functools import reduce


def dynamic_reducer(number, symbol):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element: operators[symbol](total, element)), number)



print(dynamic_reducer([1, 2, 3], '+'))
