def show_data():
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data():
    with open('book.txt', 'r', encoding='utf-8') as f:
        head = f.readline()
    if head == '':
        head = 'Ф.И.О.               | телефон\n'
    else:
        head = '\n'

    fio = input('Введите ФИО: \n').upper()
    phone_num = input('Введите номер:\n')
    
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'{head}{fio} | {phone_num}')


def find_data():
    data = input('Введите данные для поиска:\n').upper()
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book, data))


def search(book, info):
    book = book.split('\n')
    find_list = [post for post in book if info in post]
    print(f'Найдено записей: {len(find_list)}')
    return '\n'.join(find_list)


def delete_data():
    data = input('Введите данные для поиска:\n').upper()
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    list_book = search(tel_book, data).split('\n')
   
    ind_post = -1
    if len(list_book) > 1:
        for ind, item in enumerate(list_book):
            print(ind + 1, item)
        print(f'Укажите какую запись редактировать, от 1 до {len(list_book)}:')
        ind_post += int(input())
    else:
        ind_post = 0
    edit_post = str(list_book[ind_post])
    print(f'Редактируем запись: {edit_post}')

    new_lines = []
    with open('book.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
           if line.strip() != edit_post.strip():
                new_lines.append('\n' + line.strip())

    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(new_lines))



def change_data():
    delete_data()
    add_data()