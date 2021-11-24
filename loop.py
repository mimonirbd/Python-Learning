# increment
i = 0
while i <= 10:
    print(i)
    i = i + 1

print('\n')
j = 0
while j <= 40:
    print(j)
    j = j + 4

# decrement
print('\n')
i = 10
while i >= 0:
    print(i)
    i = i-1

# namota
number = 4
j = 1
while j <= 10:
    print(number, 'x', j, '=', number*j)
    j = j + 1


# user login form message
def login():
    password = True
    while password != 'admin':
        password = input('Enter your password: ')
        if password == 'admin':
            print("Login success.")
        else:
            print('Your entered pass is incorrect.')


login()

