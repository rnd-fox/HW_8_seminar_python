






























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
