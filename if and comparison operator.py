# uses of simple if else
name = 'Monir'
if name == 'monir':
    print('You are', name)
else:
    print('You aren\'t', name)

# use of if elif else  (comparison)
print('Type today\'s Name')
todayName = input()
if todayName == 'Friday':
    print('Today is Friday. So, you can sleep.')
elif todayName == 'Saturday':
    print('Wake and go to school.')
else:
    print('I don\'t know today\'s routine')


# if elif else using function method

def notice(day):
    print('Type today\'s name: ')
    today = input()
    if today == 'Friday':
        print('You can Sleep😴')
    elif today == 'Saturday':
        print('Wake up.')
    else:
        print('Sorry man, I don\'t know your today\'s routine!')


notice(notice)  # printout notice by days. Assigned notice values on notice function.


# comparison
def voter(age):
    print('Type your age: ')
    age = int(input())
    if age == 18:
        print('You are new voter.')
    elif age > 18:
        print('You are allowed to vote.')
    else:
        print('You are not allowed to vote.')


voter(voter)


# uses of nested if
def result(marks):
    print('Write any subject marks: ')
    marks = int(input())
    if marks >= 33:
        if marks >= 80:
            return 'You are A+'
        else:
            return 'You are non A+.'
    else:
        return 'Fail'


print(result(result))


# same result like upper just using elif
def result(marks):
    print('Write any subject marks: ')
    marks = int(input())
    if marks == 33:  # just replace >= with ==
        return 'You have passed.'
    elif marks >= 80:
        return 'You are A+'
    else:
        return 'You are fail.'


print(result(result))