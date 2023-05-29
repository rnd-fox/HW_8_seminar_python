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

def Delete():
    name, phone = view.Record('УДАЛЯЕМ КОНТАКТ:')
    for i in range(len(contacts)):
        if contacts[i]["name"] == name and contacts[i]["phone"] == phone:
            yes = 1
            contacts.pop(i)
            break
        else:
            yes = 0
    view.Success(yes)
    if yes == 1:
        Save()   

def Search():
    temp_list = []
    name = view.Name_contact()
    for i in contacts:
        if i["name"] == name:
            temp_list.append(i)
    view.Conclusion(temp_list)

def Edit():
    name, phone = view.Record('РЕДАКТИРОВАНИЕ КОНТАКТА')
    for i in contacts:
        if i["name"] == name and i["phone"] == phone:
            new_name, new_phone = view.Record('ОБНОВЛЕННЫЙ КОНТАКТ:')
            i["name"] = new_name
            i["phone"] = new_phone
            break
    Save()
    return

