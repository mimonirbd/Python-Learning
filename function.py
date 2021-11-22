def jobs():
    print('SEO')
    print()
    print('Video editor')


jobs()


def twoNumbers(first, second):
    totalNumber = first + second
    print(totalNumber)


twoNumbers(4, 2)


# return function
def addNumber(firstN, secondN, thirdN):
    result = firstN * secondN + thirdN
    return result


# print function replaced with own made function addNumber
print('=', addNumber(4, 5, 0))

# another example
mi = 4
si = 4
bi = 6
print(addNumber(mi, si, bi))