a = b = c = 0

# id все ссылаются на один и тот же обьект
print(a, b, c)
print(id(a), id(b), id(c))


print("....................................   перемена данных\n")

a, b = 1, 2
print(a, b )

a, b = b, a
print(a, b)

print("....................................   \n")