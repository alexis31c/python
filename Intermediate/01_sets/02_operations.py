set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Union de conjuntos
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Interseccion de conuntos, se obtiene el valor que tienen en comun
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#Se le resta el valor que tiene en comun con el otro conjunto
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#Se obtienen todos los valores a excepcion del valor que tienen en comun 
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)