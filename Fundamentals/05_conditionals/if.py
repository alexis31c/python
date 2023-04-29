if True:
    print("Esto deberia ejecutarse")

if False:
    print("Esto no deberia ejecutarse")

age=  int(input("Cual es tu edad?"))

if age >= 18 and age < 60:
    print("Eres mayor de edad")
elif age <= 18 and age > 0:
    print("Eres menor de edad")
else:
    print("Ya eres una persona de edad mayor")
