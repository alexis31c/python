
# No aceptan duplicados
set_countries={'col','mex','bol','bol'}
print(set_countries)
print(type(set_countries))

#No tienen orden
set_types = {1, 'hola', False, 12.12}
print(set_types)

#conuntos apartir de objetos
set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

#transformar a lista 
unique_numbers = list(set_numbers)
print(unique_numbers)

#CRUD
set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove

set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)
set_countries.clear()
print(set_countries)
print(len(set_countries))