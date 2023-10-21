import secrets
import string


def generate_password(length=12):
    # Define a pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Initialize an empty list to store the password characters
    password = []

    # Ensure that the generated password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))

    # Generate the remaining characters
    remaining_length = length - 4  # Account for the 4 required characters
    password.extend(secrets.choice(characters) for _ in range(remaining_length))

    # Shuffle the password characters to ensure randomness
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the desired password length: "))

    if num_passwords <= 0 or password_length <= 0:
        print("Please enter valid input.")
        return

    for _ in range(num_passwords):
        password = generate_password(password_length)
        print("Generated password: ", password)


if __name__ == "__main__":
    main()
