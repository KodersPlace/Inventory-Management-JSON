import json
from menu import menu


def login(i_username, i_password):
    with open('data.json', 'r') as j_f:
        data = json.load(j_f)
        credentials = data['credentials']
        username = credentials['username']
        password = credentials['password']

        if i_username != username or i_password != password:
            return False
        else:
            return True


def main():
    print("\t"*3 + "-"*5 + "LOGIN" + "-"*5)
    username = input('Enter username: ').strip()
    password = input('Enter password: ').strip()

    if login(username, password):
        print('Logged in sucessfully!')
        menu()
    else:
        print('Please enter correct username & password')
        return main()


if __name__ == "__main__":
    main()
