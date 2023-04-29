x=3.3
print(x)
y=1.1 +2.2
print(y)
print(x == y)

y_str = format(y, ".1g")
print("str =>",y_str)

y_str = format(y, ".2g")
print("str =>",y_str)

print("*" * 20)

print(y,x)
tolerance=0.00001
print(abs(x - y) < tolerance)

