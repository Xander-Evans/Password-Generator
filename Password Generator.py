import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','?','|','{','}','[',']']

print("Welcome to the PyPassword Generator")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))
num_of_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""

for num in range(1,num_of_letters + 1):
        password += random.choice(letters)
for num in range(1,num_of_symbols + 1):
    password += random.choice(symbols)
for num in range(1, num_of_symbols + 1):
    password += random.choice(numbers)

print(password)
random.shuffle(list(password))
password = str(password)
print(f"Your password is {password}")
