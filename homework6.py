my_dict={'Denis': 1986, 'Vadim': 1990, 'Katya': 1994}
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Sasha'))
my_dict.update({'Sasha': 1960, 'Inna': 1967})
print(my_dict)
a=my_dict.pop('Inna')
print(a)
print(my_dict)

my_set ={1,1,2,2,3,3,4,4,5,5,'Denis','Denis',True,(1,2,3,4,5)}
print(my_set)
my_set.add(6)
my_set.add(7)
print(my_set)
my_set.remove(3)
print(my_set)
