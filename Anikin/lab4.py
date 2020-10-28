# Эта фугкция позволяет перевести строку формата IP в десятичный вид из двоичного
def iptodec(ip):
    output = ''
    words = ip.split('.')
    dec = []
    i = 0
    for word in words:
        try:
            output = output + str(int(word, base=2)) + '.'
        except ValueError:
            continue
    return output

# Эта функция генерирует маску из битов под нее (биты на подсети + биты класса)
def maskgen(bits):
    mask = ''
    i = 1
    while len(mask) <= 35:
        # Пока биты не закончатся, заполняем единицами
        if bits > 0:
            mask = mask + '1'
        # Биты закончились - заполняем нулями
        else:
            mask = mask + '0'
        # После каждого восьмого символа ставим точку
        if (i % 8) == 0:
            mask = mask + '.'
        bits = bits - 1
        i = i + 1
       
    return mask


# Основной поток main
ipclass = input('\n\nВведите класс IP адреса: ')
if ipclass == 'A':
    netbits = 8
elif ipclass == 'B':
    netbits = 16
elif ipclass == 'C':
    netbits = 24
else:
    print('\n--[Неверно введен класс IP адреса]--')
    exit()
try:
    subnet = int(input('Введите количество подсетей: '))
except ValueError:
    print('--[Неверный ввод!]--')
    exit()
try:
    hosts = int(input('Введите количество компьютеров: '))
except ValueError:
    print('--[Неверный ввод!]--')
    exit()

# Вычисляем биты на подсети (по методичке)
subnetbits = 0
while (2 ** subnetbits) < subnet:
    subnetbits = subnetbits + 1

# Можно ли создать сеть
if (2 ** (32 - subnetbits - netbits)) - 2 >= hosts:
    # Генерируем маску, если условие выше верно. Количество битов маски = биты подсетей + биты класса
    print('\nМаска в двоичном виде: ' + maskgen(subnetbits + netbits))
    print('Маска в десятичном формате:\t' + iptodec(maskgen(subnetbits + netbits)))
    print('================ Переменные ================')
    print('subnetbits: ' + str(subnetbits) + '\tnetbits: ' + str(netbits) + '\thostbits: ' +
                                str(32 - subnetbits - netbits))
# Условие неверно
else:
    print('--[Невозможно создать сеть!]--')
    print('================ Переменные ================')
    print('subnetbits: ' + str(subnetbits) + '\tnetbits: ' + str(netbits) + '\thostbits: ' +
                                str(32 - subnetbits - netbits))