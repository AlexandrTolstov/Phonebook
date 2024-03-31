from random import *
import json

phonebook = {}

def save():
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Наш телефонный справочник был успешно сохранен в файле phonebook.json")
    
def load():
    with open("phonebook.json", "r", encoding="utf-8") as file: 
        return json.loads(file.read())

try:
    phonebook = load()
    print("Фильмы загружены")
except:
    print("Что-то пошло не так")
    phonebook['Вадим Пупкин'] = { 'phones': [12421432432, 1234323234], 'birthday': '01.01.1960', 'email': "vadim@mail.ru" }
    phonebook['Людмила Зайцева'] = { 'phones': [14312412235] }

while True:
    command=input("Введите команду ")
    if command == "/start":
        print("Вы открыли телефонный справочник ")
    elif command =="/stop":
        save()
        print("Вы закрыли телефонный справочник. Заходите еще, будем рады!")
        break
    elif command == "/all":
        print("Вот текущий список контактов ")
        print(phonebook)
    elif command == "/add":
        Name = ''
        Phones = []
        Birthday = ''
        Email = ''
        
        Name = input("Введите Имя нового контакта ")
        while True:
            
            while True:
                phone = input("Введите номер телефона: ")
                Phones.append(phone)
                com = input("Хотите продолжить добавления номера телефона, если ДА наберите: Y, если НЕТ наберите: N - ")
                if com == 'N':
                    break
                elif com != 'Y':
                    print("Введена неверная команда, попробуйте снова")
            break 
             
        while True:   
            com = input("Хотите добавить дату рождения, если ДА наберите: Y, если НЕТ наберите: N - ")
            if com == 'Y':
                Birthday = input("Введите дату рождения - ")
                break
            elif com == 'N':
                break
            elif com != 'Y':
                print("Введена неверная команда, попробуйте снова")
            
        while True:   
            com = input("Хотите добавить email если ДА наберите: Y, если НЕТ наберите: N - ")
            if com == 'Y':
                Email = input("Введите Email")
                break
            elif com == 'N':
                break
            elif com != 'Y':
                print("Введена неверная команда, попробуйте снова")
        
        phonebook[Name] = { 'phones': Phones }
        
        if len(Phones) != 0:
            phonebook[Name]['phones'] = Phones
        
        if Birthday != '':
            phonebook[Name]['birthday'] = Birthday
            
        if Email != '':
            phonebook[Name]['email'] = Email
        print("Фильм был успешно добавлен в коллекцию!")
        
    # elif command == "/correct":
    #     Name = ''
    #     Phones = []
    #     Birthday = ''
    #     Email = ''
        
    #     Name = input("Введите имя контакта, который нужно откорректировать ")
    #     if phonebook.get(f):
            
            
            
    #         print("Контакт изменен")
    #     else:
    #         print("Такого контакта не существует")
    
           
        
    elif command == "/help":     
        with open('Readme.md', encoding='utf-8') as f:
            text = f.read()
            print(text)
        
    
    elif command == "/delet":
        f = input("Введите имя контакта, который нужно удалить ")
        try:
            del phonebook[f]
            print("Контакт успешно удален")
        except:
            print("Такого контакта нет в телефонной книге!")
    elif command == "/save":
        save()
    elif command == "/load":
        phonebook = load()
        print("Телефонная книга успешно загружена")
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")
        