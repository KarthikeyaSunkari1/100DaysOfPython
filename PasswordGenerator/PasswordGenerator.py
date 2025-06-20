print("""     
     .--------.
    / .------. 
   / /        \ 
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |      |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'""")
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

print("Welcome to the PyPassword Generator: ")
a = int(input("Enter the number of letters you want: "))
b = int(input("Enter the number of numericals you want: "))
c = int(input("Enter the number of symbols you want: "))

password_list = []

for _ in range(a):
    password_list.append(random.choice(alphabets))

for _ in range(b):
    password_list.append(str(random.choice(numbers)))  # Convert number to string

for _ in range(c):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char  # char is now always a string

print(f"Your password is: {password}")