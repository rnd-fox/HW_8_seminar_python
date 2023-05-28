import model

def greetings():
    print('Всем пока-пока')
    return None

def menu():
    print('СПИСОК КОМАНД:')
    print('1 - вывод справочника')
    print('2 - добавление контакта')
    print('3 - редактирование контакта')
    print('4 - поиск контакта')
    print('5 - удаление контакта')
    print('0 - ВЫХОД')

def Conclusion(list_to_display = model.contacts):
    for i in list_to_display:
        print(f'Имя: {i["name"]}, \tтел: {i["phone"]}')


def Record(mode):
    name = Name_contact()
    phone = input('ВВЕДИТЕ ТЕЛЕФОН -> ')
    print(mode)
    print(f'ИМЯ: {name}, \tтел: {phone}')
    return (name, phone)

def Success(yes):
    if yes == 0:
        print('ЧТО-ТО ПОШЛО НЕ ТАК, ПОВТОРИТЕ ПОПЫТКУ')
    else:
        print('КОНТАКТ УДАЛЕН')
    return

def Name_contact():
    name = input('ВВЕДИТЕ ИМЯ КОНТАКТА -> ')
    return name


