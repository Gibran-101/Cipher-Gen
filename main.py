import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to CIPHER GENERATOR!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

random_letters=[]
for letter in range(1, nr_letters+1):
  random_letters.append(random.choice(letters))
  toStringLetters = ''.join(random_letters)
random_nums = []
for nums in range(1, nr_numbers+1):
  random_nums.append(random.choice(numbers))
  toStringNums = ''.join(random_nums)
random_symbs = []
for symbs in range(1, nr_symbols+1):
  random_symbs.append(random.choice(symbols))
  toStringSymbs = ''.join(random_symbs)
passwordMix = (toStringLetters + toStringNums + toStringSymbs)
password = ''.join(random.sample(passwordMix, len(passwordMix)))
print(f"Your password: {password}")
