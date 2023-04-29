#CRUD Create, Read, Updates & Delete

numbers=[1,2,3,4,5]
print(numbers[1])
numbers[-1]=10
print(numbers)

numbers.append(11)
print(numbers)
numbers.insert(0,0)

#Se puede agregar otro tipo de dato
numbers.insert(1,"Hola") 
print(numbers)

numbers2 = [12,13,14,15,15]
new_numbers=numbers + numbers2
print(new_numbers)

#Obtner el index de algun valor
index=new_numbers.index("Hola")
new_numbers.pop(index)
print(new_numbers)
new_numbers.pop()
#Elimina el ultimo valor cuando no tiene parametro de entrada
print(new_numbers)

#Eliminar un registro de la lista por su valor
new_numbers.remove(0)
print(new_numbers)

new_numbers.reverse()
print(new_numbers)

ran_numbers=[1,4,2,5,6,8,2]
ran_numbers.sort()
print(ran_numbers)

ran_string=["sd","ed","gt"]
ran_string.sort()
print(ran_string)

#No se puede usar sort cuando la lista es de diferentes tipos de datos.
