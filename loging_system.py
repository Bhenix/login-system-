print('Welcome to Eternal web')
account = {}
try:
    with open('account.txt','r') as file:
        for line in file:
            user_name, user_password = line.strip().split(':')
            account[user_name] = user_password
except FileNotFoundError:
    pass 

while True:
    print(f'\n1. sign Up')
    print(f'2. Login')
    print(f'3. Exit')

    state = int(input('Select your choice'))

    if state == 1:
        user_name = input('Create username: ')
        user_password = input('Create password: ')
        account[user_name] = user_password
    

        print('Account successfully created')

    elif state ==2:
        print('Login')
        user_login = input('Enter username: ')
        login_pass = input('Enter password: ')
        if user_login in account and account [user_login] == login_pass :
            print(f'{user_login} You are Welcome once aagin\nWe have missed your pressence')
        else:
            print('Invalid username or password')
    elif state ==3:
        print('Goodbye')
        break 
    else:
        print('Do the right thing ')