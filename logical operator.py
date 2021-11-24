# roller coaster condition
def rollerCoaster(age, height):
    if age > 5 and height >= 40:
        if age < 19 and height < 60:
            return 'You can ride.'
        else:
            return 'you don\'t have permission to ride.'
    else:
        return 'You can not ride.'


print(rollerCoaster(17, 40))
print(rollerCoaster(19, 61))
print(rollerCoaster(4, 400))
