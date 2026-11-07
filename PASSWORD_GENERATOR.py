import secrets
import string

char_p=string.ascii_letters+string.digits+string.punctuation

length=int(input("Enter a length :"))

password=""

for i in range(length):
    password+=secrets.choice(char_p)

print("\nYour Generated Password: ",password)
