text = input("Dime que tecnología estas aprendiendo =>")

if "Python" in text:
    print("Perfecto, gran tecnoligía")
else:
    print("Perfecto es una gran tecnología tambien")

size= len(text)
print(size)

# Metodos que tienen las strings
print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith("Estoy"))
print(text.endswith("C#"))
print(text.replace("Python","JavaScript"))

text_2="este es un titulo"
print(text)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("12".isdigit())
print("12.1".isdigit())



