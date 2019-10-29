base = {'KateWhite25f': {'name': 'kate', 'surname': 'white', 'age': 25, 'sex': 'f'},
        'JackSparrow35m': {'name': 'jack', 'surname': 'sparrow', 'age': 35, 'sex': 'm'},
        'NickLop27m': {'name': 'nick', 'surname': 'lop', 'age': 25, 'sex': 'm'}}


def save():
    user_name = input('Enter your name: ').lower()
    user_surname = input('Enter your surname: ').lower()
    user_age = input('Enter your age: ')
    while not user_age.isnumeric():
        user_age = input('Wrong! Enter a NUMBER (age): ')

    user_sex = input('Enter your sex ([m]ale, [f]emale): ').lower()

    _id = user_name + user_surname + str(user_age) + user_sex

    base[_id] = {}
    base[_id]['name'] = user_name
    base[_id]['surname'] = user_surname
    base[_id]['age'] = int(user_age)
    base[_id]['sex'] = user_sex

    print(f'User {user_name.title()} {user_surname.title()} of age {user_age} was added')


def search(**kwargs):
    user_find = str()
    for i in kwargs:
        user_find = kwargs[i]

    a = [{_id: info} for _id, info in base.items() for key in info if user_find in str(info[key])]

    if a:
        for key in a:
            for _id, info in key.items():
                print(f"User was found: {info['name'].title()}, {info['surname'].title()}, age: {info['age']}, "
                      f"sex: {info['sex']}")
            else:
                continue
    else:
        print("Can't find. Try again")


while True:
    cmd = input('What do you want to do? [f]ind a user? Or [a]dd a new one? To exit type [x]: ').lower()

    if cmd == 'f':
        find_cmd = input("Choose how to find: 1.name, 2.surname, 3.name+surname or 4.age: ")
        if find_cmd == '1':
            find_name = input("Enter the name: ").lower()
            search(name=find_name)
        elif find_cmd == '2':
            find_surname = input("Enter the surname: ").lower()
            search(surname=find_surname)
        elif find_cmd == '3':
            find_name, find_surname = input("Enter the name and surname: ").lower().split()
            search(name=find_name, surname=find_surname)
        elif find_cmd == '4':
            find_age = input("Enter the age: ")
            search(age=find_age)

    elif cmd == 'a':
        save()

    elif cmd == 'x':
        print('Ok, exit the program....')
        break

    elif cmd != 'a' or 'f' or 'x':
        print('The command is not defined, please enter [f] or [a] or [x].')