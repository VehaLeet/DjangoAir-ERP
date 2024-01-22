import functools

# numbers = [1, 2, 3, 4, 5]
# product = functools.reduce(lambda x, y: x * y, numbers)
# print(product)
# product = map(lambda x, y: x * y, numbers)
# for p in product:
#     print(p)


def multiply(x, y, z):
    return x * y * z


multipy_by_6 = functools.partial(multiply, 2, 3)

result = multipy_by_6(4)
print(result)
