print('Type Your Total Earnings: ')
earning = int(input())
print('Type total Comments: ')
comment = int(input())

if earning >= 100 and comment >= 50:
    eligible = True
else:
    elig = False

if elig:
    print('You can do free course.')
else:
    print('You have to pay 1 Thousands.')

