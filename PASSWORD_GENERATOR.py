import secrets
import string

char_p=string.ascii_letters+string.digits+string.punctuation

length=12

password=""

for i in range(length):
    password+=secrets.choice(char_p)

print("\nYour Generated Password: ",password)
