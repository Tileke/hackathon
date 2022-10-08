import json
import datetime

FILE_PATH = 'data.json'

# data = [
#     {
#         'id': 1,
#         'name': 'product1',
#         'price': 99,
#         'created_at': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
#         'updated_at': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
#         'description': 'description for product1',
#         'is_active': 'selling'
#     }
# ]

# with open(FILE_PATH, 'r+') as file:
#     json.dump(data, file)

def get_data(ge_price=None, le_price=None, activity=None):
    with open(FILE_PATH) as file:
        data = json.load(file)
    if ge_price:
        data = [i for i in data if i['price'] >= float(ge_price)]
    if le_price:
        data = [i for i in data if i['price'] <= float(le_price)]
    if activity == 'selling':
        data = [i for i in data if i['is_active'] == activity]
    elif activity == 'sold':
        data = [i for i in data if i['is_active'] == activity]
    return data 

def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data[0]
    return 'Item not found'

def post_data():
    data = get_data()
    max_id = max([i['id'] for i in data])
    data.append({
        'id': max_id + 1,
        'name': input('Enter item name: '),
        'price': float(input('Enter item price: ')),
        'created_at': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
        'updated_at': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
        'description': input('Enter item description: '),
        'is_active': 'selling'
    })
    json.dump(data, open(FILE_PATH, 'w'))
    return 'Item uploaded'    

def update_data(id):
    data = get_data()
    data_update = [i for i in data if i['id'] == id]
    if data_update:
        index_data = data.index(data_update[0])
        if input('Do you want to change product name? \n(yes/no) \n: ') == 'yes'.lower():
            data[index_data]['name'] = input('Enter new name: ')
        if input('Do you want to change product price? \n(yes/no) \n: ') == 'yes'.lower():
            data[index_data]['price'] = float(input('Enter new price: '))
        if input('Do you want to change product description? \n(yes/no) \n: ') == 'yes'.lower():
            data[index_data]['description'] = input('Enter new description: ') 
        if input('Do you want to change product activity status? \n(yes/no) \n: ') == 'yes'.lower():   
            activity_status = input('Enter "selling" or "sold": ').lower()
            if activity_status == 'selling' or activity_status =='sold':
                data[index_data]['is_active'] = activity_status
            else:
                return 'Incorrect activity status!'
        data[index_data]['updated_at'] = datetime.datetime.now().strftime('%m/%d/%Y, %H:%M%:%S')
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Update succesful!'
    return 'Item not found'    

def delete_data(id):
    data = get_data()
    data_delete = [i for i in data if i['id'] == id]
    if data_delete:
        data.remove(data_delete[0])
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Item succesfully deleted!'
    return 'Item not found'