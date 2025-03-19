import string

def calculate_combinations(length, character_set):
    total_characters = len(character_set)
    combinations = total_characters ** length
    return combinations

def main():
    print("Password Combination Calculator")
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase characters (y/n): ").lower() == 'y'
    include_digits = input("Include digits (y/n): ").lower() == 'y'
    include_special = input("Include special characters (y/n): ").lower() == 'y'

    character_set = lower_case
    if include_uppercase:
        character_set += upper_case
    if include_digits:
        character_set += digits
    if include_special:
        character_set += special_characters
    
    combinations = calculate_combinations(length, character_set)
    print(f"\nThe total number of possible combinations for a {length}-character password is: {combinations}")

if __name__ == "__main__":
    main()
