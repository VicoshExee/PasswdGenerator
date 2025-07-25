import random
import string 

def pass_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwd = ""
    print(characters)

    while len(passwd) < length:
        char = random.choice(characters)
        passwd += char

    return passwd

min_length = 0
while min_length < 12:
    min_length = int(input('Taille de votre mot de passe (min 12) :'))
  
print(pass_generator(min_length))
