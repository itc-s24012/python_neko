prefecture_of_japan = {1: 'Hokkaidou', 2: 'Aomori', 3: 'Iwate'}
print(prefecture_of_japan)
print(prefecture_of_japan[1])
print(prefecture_of_japan.get(0))
print(prefecture_of_japan.get(1))
print(prefecture_of_japan.get(0, 'Not Found'))
prefecture_of_japan[4] = 'Miyagi'
print(prefecture_of_japan)
print(1 in prefecture_of_japan)
del prefecture_of_japan[4]
print(prefecture_of_japan)
print(prefecture_of_japan.pop(3))
print(prefecture_of_japan)
prefecture_of_japan[3] = Iwate
print(prefecture_of_japan)
for x in prefecture_of_japan.key():
    print(x)
for x in prefecture_of_japan.values():
    print(x)
for key, x in prefecture_of_japan.item():
    print(key, x)

