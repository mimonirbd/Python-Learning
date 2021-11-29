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


# number split
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
