print('Welcome to Eternal web')
account = {}
print('Do you want to login or signUp')
state = int(input('Enter 0 to login and 1 to create account'))

if state == 1:
    user_name = input('Create username: ')
    user_password = input('Create password: ')
    account[user_name] = user_password
    account['password'] = user_password

    print('Account successfully created')

elif state ==0:
    print('Login')
    user_login = input('Enter username: ')
    login_pass = input('Enter password: ')
    if user_login in account and account [user_login] == login_pass :
        print(f'{user_login} You are Welcome once aagin\nWe have missed your pressence')
    else:
        print('Invalid username or password')
else:
    print('Do the right thing ')