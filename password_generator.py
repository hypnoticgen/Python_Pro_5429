import random
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud= int(input("que longitud quieres para tu contraseña?"))
password= ""

for i in range(longitud):
    password+= random.choice(elements)
print(password)