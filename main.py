from hackathon1 import *

def main():
    while True:
        method = input('Welcome to my mini code! \nHere is the list of functions: \n1 - get all of the products \n2 - get specific item \n3 - create new product \n4 - delete item \n5 - update item \n6 - stop the program \nEnter the number: ')
        if method == '1':
            skip_filter = input('If you do not want to filter items, type "skip" \nIf you want to filter, type "filter" \n: ').lower()
            if skip_filter == 'skip':
                print(get_data())
            else:
                print(get_data(ge_price = input('Enter number to filter more than: '), le_price = input('Enter number to filter less than: '), activity = input('Enter "selling" or "sold": ')))
        elif method == '2':
            id = int(input('Enter id of the item: '))
            print(get_one_data(id))
        elif method == '3':
            print(post_data())
        elif method == '4':
            id = int(input('Enter id of the item you want to delete: '))
            print(delete_data(id))
        elif method == '5':
            id = int(input('Enter id of the item you want to update: '))
            print(update_data(id))
        elif method == '6':
            print('Program stopped')
            break
        else:
            print('Function not found')

if __name__ == '__main__':
    main()