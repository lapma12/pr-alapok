"""
a = "Hello, world!asd"
print(a[12])
print(a[3])

for x in "banana":
    print(x , end="-")
"""
a = "Hello, world"
szamlalo = 1

for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end="")
    szamlalo = szamlalo + 1


