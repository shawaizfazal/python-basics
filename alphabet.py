

# Asking the user to type a letter or number
character = input("Enter any key on your keyboard: ")

# Checking if it's a lowercase alphabet or uppercase alphabet
if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):
    print("Yay! That is definitely an alphabet")
else:
    print("no that is not an alphabet")