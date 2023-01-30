from funcs.crud import create, read_database, update, delete

database = {}

# create(database, 'Samsung Galaxy S10', 50000)
# create(database, 'IPhone 14', 140000)

# print(read_database(database))
# print(read_database(database, 'IPhone 14'))

# update(database, 'IPhone 14', 100000)
# print(read_database(database, 'IPhone 14'))

# delete(database, 'Samsung Galaxy S10')
# print(read_database(database))

# print(read_database(database, 'MOtorola'))


# TODO: дописать тесты на update и delete
# TODO: интерфейс для управления функциями
while True:
    funcs = {
        'create': create,
        'read': read_database,
        'update': update,
        'delete': delete
    }

    action = input(
        """ 
        что вы хотите сделать?
        create
        read
        update
        delete
        """
    )

    if action == 'create':
        title = input('Введите название ')
        price = float(input('Введите цену '))
        funcs['create'](database, title, price)
    elif action == 'read':
        title = input('Введите название ')
        print(funcs['read'](database, title))
    elif action == 'update':
        title = input('Введите название ')
        price = float(input('Введите новую цену '))
        funcs['update'](database, title, price)
    elif action == 'delete':
        title = input('Введите название ')
        funcs['delete'](database, title)




