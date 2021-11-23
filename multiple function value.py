# multiple function use

def returnMultiple(number):
    square = number ** 2
    cube = number ** 3
    return square, cube  # jei value age print korte cacce seta serially age hobe.


print('Input your desired number: ')
typed = input()
print('You typed: ', typed)
typed = int(typed)
print(returnMultiple(typed))


# custom function for user input

def nameResult():
    print('Type your First name: ')
    fN = input()
    print('Your First Name is:', fN)
    print('Type your Last name: ')
    lN = input()
    print('Your last name is:', lN)
    return returnName(fN, lN)


def returnName(fN, lN):
    return fN + ' ' + lN


print('\n\tYour full name is:', nameResult())


# f2c converter function
def F2C(F):
    C = (F - 32) * (5 / 9)
    return C


print(F2C(94.4))
