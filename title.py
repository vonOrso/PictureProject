'''
Тип : title('1-10, 15-20','2-3, 5-7','1-3, 5')
В таком виде должно быть 320 названий

На выходе : ['I01_02_01.png', ...]
'''
def title(obj1,obj2,obj3):
    cif1,cif2,cif3 = obj1.split(','),obj2.split(','),obj3.split(',')
    mas1,mas2,mas3,names = [],[],[],[]

    #Массивы c номерами нужных картинок
    for i in cif1:
        mas1.extend(list(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1))) if '-' in i else mas1.append(int(i))

    for i in cif2:
        mas2.extend(list(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1))) if '-' in i else mas2.append(int(i))

    for i in cif3:
        mas3.extend(list(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1))) if '-' in i else mas3.append(int(i))

    #Создание строк
    for z in mas1:
        z = '0' + str(z) if z < 10 else str(z)

        for x in mas2:
            x = '0' + str(x) if x < 10 else str(x)

            for c in mas3:
                c = '0' + str(c) if c < 10 else str(c)
                names.append(''.join('I' + z + '_' + x + '_' + c + '.png'))

    return names










