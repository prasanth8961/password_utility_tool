import random
import string
import math


def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"


def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def estimate_brute_force_time(password):
    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char in string.punctuation for char in password):
        charset_size += len(string.punctuation)

    total_combinations = charset_size ** len(password)
    attempts_per_second = 10**9
    time_seconds = total_combinations / attempts_per_second
    return time_seconds

def spacer():
    print()

def start():
    while True:
         print("======================")
         print("Password Utility Tool")
         print("======================")
         print("1. Check Password Strength")
         print("2. Generate Secure Password")
         print("3. Estimate Brute-Force Time")
         choice = input("Enter your choice [1/2/3]: ")

         if choice == "1":
            password = input("Enter the password to check: ")
            strength = check_password_strength(password)
            print(f"[+] Password Strength >>> {strength}")
            spacer()
         elif choice == "2":
            try:
                length = int(input("Enter the desired password length (minimum 8): "))
                password = generate_password(length)
                print(f"[+] Generated Password >>> {password}")
                spacer()
            except Exception as ae:
                print(ae)
         elif choice == "3":
            password = input("Enter the password to analyze: ")
            time_seconds = estimate_brute_force_time(password)
            print(f"[+] Estimated Brute-Force Time >>> {time_seconds:.2e} seconds")
            spacer()
         else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
   start()
