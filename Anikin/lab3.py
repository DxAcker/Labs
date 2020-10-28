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

# Функция для перевода IP из десятичного в двоичный
def iptobin(ip):
    output = ''
    words = ip.split('.')
    for word in words:
        # Переведем в двоинчый (формат будет 0b11101)
        word = bin(int(word))
        # Дополним сверху нулями, чтобы формат был верный
        while len(word) <= 8:
            word = '0' + word
        # Конкатенация и уберем 0b
        output = output + word.replace('0b', '') + '.'
    return output

# Функция проверки десятичного введенного IP
def validdec(ip):
    try:
        if ip.isalpha() or ip == '':
            return False
        words = ip.split('.')
        if len(words) != 4:
            return False
        for word in words:
            if int(word) < 0 or int(word) > 255:
                return False
    except ValueError:
        return False
    return True

# Основной поток main
classip = ['A', 'B', 'C', 'D', 'E']
ip = input('\nВведите IP: ')
ipformat = input('Введенный IP в двоичной(bin) или десятичной(dec) системе счисления? ')

# Работаем с десятичным
if ipformat == 'dec':
    if validdec(ip):
        ip = iptobin(ip)
        words = ip.split('.')
        i = 0
        # Находим класс IP по методичке (положение нуля)
        for char in words[0]:
            if char == '0':
                print('  Класс IP: ' + classip[i])
                exit()
            else:
                i = i + 1  

    else:
        print('\n--[Введено неверное значение!]--')   

# Работаем с бинарным
elif ipformat == 'bin':
    try:
        if validdec(iptodec(ip)):
            words = ip.split('.')
            i = 0
            for char in words[0]:
                if char == '0':
                    print('  Класс IP: ' + classip[i])
                    exit()
                else:
                    i = i + 1
        else:
            print('\n--[Введено неверное значение!]--')
    except ValueError:
        print('\n--[Введено неверное значение!]--')
else:
    print('\n--[Введено неверное значение!]--')    
    exit()