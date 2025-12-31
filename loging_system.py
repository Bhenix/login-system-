print('Welcome to Eternal web')
account = {}
print('Do you want to login or signUp')
state = int(input('Enter 0 to login and 1 to create account'))

if state == 1:
    user_name = input('Create username: ')
    user_password = input('Create password: ')

    print('Account successfrlly created')

elif state ==0:
    print('Loging')
    user_login = input('Enter username: ')
    login_pass = input('Enter password: ')
    print(f'{user_login} You are Welcome once aagin\nWe have missed your pressence')
else:
    print('Do the right thing ')