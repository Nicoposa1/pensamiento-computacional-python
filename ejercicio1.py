name_usr_1 = input('Hola necesito el nombre de primer usuario: ')
name_usr_2 = input('Gracias ahora necesecito el nombre del segundo usuario: ')
edad_usr_1 = int(input(f'Cuantos años tiene {name_usr_1}?: '))
edad_usr_2 = int(input(f'Y la edad de {name_usr_2}?: '))

if edad_usr_1 > edad_usr_2:
    print(f'Sabias que {name_usr_1} es mayor que {name_usr_2}?')
elif edad_usr_1 < edad_usr_2:
    print(f'Sabisa que {name_usr_2} es mayor que {name_usr_1}')
else:
    print(f'Sabias que {name_usr_1} y {name_usr_2} tienen la misma edad')
