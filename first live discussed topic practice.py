# string manipulation

# blank list
blank_list = []
# split text
string_text = 'This is a full text. Convert it in full stop based.'
spliting = string_text.split(".")
print(spliting)
print(spliting[0])  # to access desired position

# list manipulation
countryNames = ['Bangladesh', 'India', 'US', 'UK']
print(countryNames[0], countryNames[2])

# print from last
print(countryNames[-1])

# add new elements on list
countryNames.append('Bhutan')  # append means add new element
print(countryNames)

# remove a specific value from list
countryNames.pop(0)  #position wise remove
print(countryNames)
countryNames.remove("US") # value wise remove
print(countryNames)


# dictioary
myDictionary = {'name':'Tahsan', 'age': 34, 'gender': 'male', 'height': 5.11}
print('The name of the singer is', myDictionary['name'] +'.', 'He is', myDictionary['age'], 'years old.')



# for loop in list
mylist = list(range(20, 31))
for theList in mylist:
    print(theList, 'is posted.')
    
    '''An example: print(theList, end= 'ms')
# If want to use anything
        within the string. Like here I wanted to add ms with every value. '''


# file read from txt file
file = open('forPythonPractice.txt', 'r', encoding='utf-8')
line = file.readlines() # if need to read full lines then command will readlines() & readline() function is for print only 1st line.
print(line)

for lines in line:
    print(lines.strip('\n'))

file.close()


# kg to pound using custom functions and split sample
def kgtoPound (number):
    splitedNumber = number.split()
    kgNumber = int(splitedNumber[0])
    poundNumber = float(kgNumber * 2.20462)
    output = str(poundNumber), 'Pounds'
    return output

print(kgtoPound('56 kg'))


# kg to pound using custom functions and split sample + TRY and EXCEPT uses. If any argument missing or error it will continue by try and except function.
def kgToPound (number):
    try:
        splitedNumber = number.split()
        kgNumber = int(splitedNumber[0])
        poundNumber = float(kgNumber * 2.20462)
        output = str(poundNumber), 'Pounds'
        return output
    except:
        return '-'  # it will show - when getting the error.
    
print(kgToPound('KG 54'))  


# how to identify he/she/him/her
def gender():
    try:
        gtype = input('Type: ')
        if gtype == 'm':
            return 'He'
        elif gtype == 'f':
            return 'She'
        else:
            return 'It'
    except:
        pass

print(gender())


# number split
try:
    numbers = input('Input 10-100): ')
    numbers = numbers.split('-')

    num1, num2 = numbers[0], numbers[1]
    print(type(num1), num1)

    # converting into int
    num1, num2 = int(numbers[0]), int(numbers[1])
    print(type(num1), num1)

    # range
    num1, num2 = int(numbers[0]), int (numbers[1]) + 1
    rangeSample = list(range(num1, num2))
    print('range value is: ', rangeSample)
except:
    pass
