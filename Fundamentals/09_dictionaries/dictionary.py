my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Alexis',
  'last_name': 'Cordero',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('avion' in my_dict)
print('otroqueno' in my_dict)

#Insert, Update and Delete

person={
    'name':'Alexis',
    'last_name':'Cordero',
    'langs':['C#','C++','Python','JavaScript'],
    'age':26
}
print(person)

person['name']='Alexis Cordero'
person['langs'].append("Go")
print(person)

del person['last_name']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())