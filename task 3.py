# Урок 5 задание 1
my_string = 'Digital Humanities'
print("строка по буквам:")
for i in my_string:
    print(i)
print("строка наоборот:", my_string[::-1],'\n')

# Урок 5 задание 2
list=['cats','dogs','mice','birds','snakes']
print('список:',list)
print('элементов в списке:',len(list))
list.append('horses')
list.append('cows')
print('добавили лошадей и коров:',list)
list.remove('snakes')
list.remove('dogs')
print('убрали змей и собак:',list, '\n')

# Урок 7
cities = (
    ('Санкт-Петербург',5600044,1439),
    ('Рим',2759620,1287),
    ('Гамбург',1814879,755.3)
)
print('Информация о Санкт-Петербурге:')
print('Название:', cities[0][0])
print('Население:', cities[0][1], 'человек')
print('Площадь:', cities[0][2], 'км^2\n')

print('Информация о Риме:')
print('Название:', cities[1][0])
print('Население:', cities[1][1], 'человек')
print('Площадь:', cities[1][2], 'км^2\n')

print('Информация о Гамбурге:')
print('Название:', cities[2][0])
print('Население:', cities[2][1], 'человек')
print('Площадь:', cities[2][2], 'км^2/n')