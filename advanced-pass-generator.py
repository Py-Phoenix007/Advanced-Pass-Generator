import random

def generate_password(length=12,
 use_uppercase=True,
 use_lowercase=True,
 use_digits=True,
 use_special=True,
 num_passwords=1):
    characters = ''
    if use_uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lowercase:
        characters += 'abcdefghijklmnopqrstuvwxyz'
    if use_digits:
        characters += '0123456789'
    if use_special:
        characters += '!@#$%^&*()-_=+[]{};:,.<>/?|'

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected category
    passwords = []
    for _ in range(num_passwords):
        password = []

        if use_uppercase:
            password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if use_lowercase:
            password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        if use_digits:
            password.append(random.choice('0123456789'))
        if use_special:
            password.append(random.choice('!@#$%^&*()-_=+[]{};:,.<>/?|'))

        # Fill the remaining length of the password
        remaining_length = length - len(password)
        if remaining_length > 0:
            password += random.choices(characters, k=remaining_length)

        # Shuffle the password to ensure randomness
        random.shuffle(password)
        passwords.append(''.join(password))

    return passwords

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    num_passwords = int(input("How many passwords would you like to generate? "))

    generated_passwords = generate_password(length,
     use_uppercase,
     use_lowercase,
     use_digits,
     use_special,
     num_passwords)
    for i, pwd in enumerate(generated_passwords, 1):
        print(f"Generated Password {i}: {pwd}")