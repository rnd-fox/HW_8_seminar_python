import os.path
# здесь описана модель телефонного справочника
contacts = [{"name": "", "phone": ""}]

def Read(filename='contacts.txt', clear=True):
    if os.path.isfile(filename): #являеться ли путь файлом
        if clear:
            contacts.clear()
        rd = open(filename, 'r', encoding='utf-8')
        for line in rd:
            spline = line.split(';')
            write = {"name": spline[0], "phone": spline[1].rstrip()}
            contacts.append(write)
        rd.close()

def Save(filename='contacts.txt'):
    with open(filename, 'w',encoding='utf-8') as save:
        for i in contacts:
            save.write('{};{}\n'.format(i["name"], i["phone"]))

def Conclusion():
    view.Conclusion()

def Add():
    name, phone = view.Record('ДОБАВЛЕН КОНТАКТ:')
    new_record = {"name": name, "phone": phone}
    contacts.append(new_record)
    with open('contacts.txt', 'a', encoding='utf-8') as add:
        add.write('{};{}\n'.format(name, phone))
