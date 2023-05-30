import view
import model

def start():
    view.greetings()
while True:
    view.menu()
    sel=int(input(f'--- введите команду ---> '))
    if sel==0:
        break
    elif sel==1:
        model.Conclusion()
    elif sel==2:
        model.Add()
    elif sel==3:
        model.Edit()
    elif sel==4:
        model.Search()
    elif sel==5:
        model.Delete()
    else:
        print('Данной команды не сущестует, попробуйте еще раз')



if __name__ == '__main__':
    start()