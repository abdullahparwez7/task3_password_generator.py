import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                return length

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_yes_no_choice(message):
    while True:
        choice = input(message).strip().lower()

        if choice == "yes" or choice == "y":
            return True
        elif choice == "no" or choice == "n":
            return False
        else:
            print("Invalid input. Please enter yes or no.")


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if characters == "":
        print("Error: Please select at least one character type.")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_number:
        score += 1

    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def show_password_details(password):
    print("\n---------- GENERATED PASSWORD ----------")
    print(password)
    print("----------------------------------------")
    print(f"Password Length: {len(password)}")
    print(f"Password Strength: {check_password_strength(password)}")
    print("----------------------------------------")


def main():
    print("========== ADVANCED PASSWORD GENERATOR ==========")

    while True:
        length = get_password_length()

        use_uppercase = get_yes_no_choice(
            "Do you want uppercase letters? (yes/no): "
        )

        use_lowercase = get_yes_no_choice(
            "Do you want lowercase letters? (yes/no): "
        )

        use_numbers = get_yes_no_choice(
            "Do you want numbers? (yes/no): "
        )

        use_symbols = get_yes_no_choice(
            "Do you want special characters? (yes/no): "
        )

        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )

        if password is not None:
            show_password_details(password)

        again = get_yes_no_choice(
            "\nDo you want to generate another password? (yes/no): "
        )

        if again is False:
            print("Thank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
