import math

def square(side):
    area = side * side
    return math.ceil(area)

result = square(2)
print(result)