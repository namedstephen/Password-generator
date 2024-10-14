
import random, string, time

def generate_password(min_lenght, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while meet_criteria == False or len(password) < min_lenght:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True 
        
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
        
    return password

min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want the password to have numbers(y/n) ? ").lower() == ("y" or "yes" or "ye")
has_special = input("Do you want the password to have special characters(y/n) ? ").lower() == ("y" or "yes" or "ye")
print("Password is generating...")
time.sleep(2)
password = generate_password(min_lenght,has_number, has_special)
print("Your password is:", password)
time.sleep(4)
