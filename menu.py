import json
from random import random


def add_product():
    # product name
    # price
    product_name = input('Enter product name: ').strip()
    price = float(input('Enter price: ').strip())

    if not product_name:
        print('Please fill all the fields correctly ...')
        return add_product()

    product_id = str(int(random() * 10000))
    with open('data.json', 'r') as j_f:
        data = json.load(j_f)
        data['products'][product_id] = {
            "name": product_name,
            "price": price
        }
        with open('data.json', 'w') as j_f:
            json.dump(data, j_f, indent=2, sort_keys=True)


def view_product():
    with open('data.json','r') as j_f:
        data=json.load(j_f)
        for product_id, product in data['products'].items():
            print(f"Product ID: {product_id}")
            print(f"Product Name: {product['name']}")
            print(f"Price: {product['price']}")
            print("-" * 10)

def search_product():
    product_name = input('Search product: ').strip()
    with open('data.json', 'r') as j_f:
        data = json.load(j_f)
        for product_id, product in data['products'].items():
            if product['name'].find(product_name) > -1:
                print(f"Product ID: {product_id}")
                print(f"Product Name: {product['name']}")
                print(f"Price: {product['price']}")
                print("-"*10)


def update_product():
    product_id = input('Enter product id: ').strip()
    if not product_id:
        print("Please enter a valid id ...")
        return update_product()

    with open('data.json', 'r') as j_f:
        data = json.load(j_f)
        ids = data['products'].keys()
        if product_id not in ids:
            print("Please enter a valid id ...")
            return update_product()

        u_product_name = input('Enter updated product name: ').strip()
        u_price = float(input('Enter updated price: ').strip())

        if not u_product_name:
            u_product_name = data['products'][product_id]['name']

        if not u_price:
            u_price = data['products'][product_id]['price']

        updated_product = {
            "name": u_product_name,
            "price": u_price
        }

        data['products'][product_id] = updated_product

        with open('data.json', 'w') as j_f:
            json.dump(data, j_f,indent=2, sort_keys=True)


def delete_product():
    product_id = input('Enter product id: ').strip()
    if not product_id:
        print("Please enter a valid id ...")
        return update_product()

    with open('data.json', 'r') as j_f:
        data = json.load(j_f)
        ids = data['products'].keys()
        if product_id not in ids:
            print("Please enter a valid id ...")
            return update_product()

        data['products'].pop(product_id)

        with open('data.json', 'w') as j_f:
            json.dump(data, j_f,indent=2, sort_keys=True)


def menu():
    # C_UD
    print('\t\t----------WELCOME TO INVENTORY----------')
    print('1- Add product')
    print('2- Search product')
    print('3- View Products')
    print('4- Update product')
    print('5- Delete product')
    print('6- Exit')

    option = int(input('Enter option: ').strip())

    if option == 6:
        return

    if option < 1 or option > 5:
        print('Invalid option')
        input('Press <enter> key to continue ...')
        return menu()

    if option == 1:
        add_product()
    elif option == 2:
        search_product()
    elif option==3:
        view_product()
    elif option == 4:
        update_product()
    else:
        delete_product()

    return menu()
