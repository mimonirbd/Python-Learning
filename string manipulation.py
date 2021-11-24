# capitalise, lower, strip, replace, split, len
title = input('Type your title: ')
print('1st:', title)  # simple view
print('2nd:', title.capitalize())  # capitalize the first letter of a first line..
print('3rd:', title.lower())  # convert lower case your typing every letter/word/sentences.
print('4th:', title.strip())  # by default remove the unwanted spaces from line starting and ending point.
print('5th:', title.lstrip())  # it can remove unwanted space from line left (starting point).
# to remove the ending point spaces use rstrip().
print('6th:', title.strip('.'))  # when need to remove custom character

title2 = input('Input a sentence/word that contains \'bd\': ')
print('7th:  ', title2.replace('bd', 'India.'))

# if you want to replace/convert title text into URL.
url = input('Type post title: ')
print('8th: ', url.strip().lower().replace(' ', '-'))

print(url.split())  # split means separate every single word to list item.
