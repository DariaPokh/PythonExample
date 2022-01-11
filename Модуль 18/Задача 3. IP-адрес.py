ip_address_list = []

for i in range(4):
    number = int(input('Введите число № {index} : '.format(index=i+1)))
    while number < 0 or number > 255:
        number = int(input('Неверный ввод. Введите число еще раз: '))
    ip_address_list.append(number)

ip_address = '{0}.{1}.{2}.{3}'.format(ip_address_list[0], ip_address_list[1], ip_address_list[2], ip_address_list[3])
print(ip_address)

