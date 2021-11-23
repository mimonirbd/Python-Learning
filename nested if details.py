# get number status
def numStatus(number):
    print('Type any number to get it\'s status: ')
    number = int(float(input()))
    if number > 0:
        return 'It\'s positive number'
    elif number < 0:
        return 'It is negative number.'
    else:
        return 'It\'s Zero'


print(numStatus(numStatus))


# get the status: Is it square?
def isSquare(value):
    print('Type width: ')
    width = int(input())
    print('Type height: ')
    height = int(input())
    print('Type height: ')
    if width == height:
        print('It\'s Square')
        # return 'It is Square'
    else:
        print('Not square.')
        # return 'Not square.'


# if uses 'print' on condition then use just function name. But if uses 'return' then use print function.
isSquare(isSquare)


# get the status of rectangle or not
def isRectangle():
    print('Type 1st width, 1st height, 2nd width, 2nd height: ')
    width1, height1, width2, height2 = input(), input(), input(), input()
    if width1 == width2:
        if height1 == height2:
            return 'It is rectangle'
    else:
        return 'Not rectangle.'


print(isRectangle())

