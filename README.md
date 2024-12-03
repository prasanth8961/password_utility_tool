# Password Utility Tool 🛡️

A simple Python project designed to enhance cybersecurity awareness by providing tools to evaluate password strength, generate secure passwords, and estimate brute-force attack time.

---

## Features

1. **Password Strength Checker**
   - Analyzes the strength of a password based on:
     - Length
     - Use of uppercase and lowercase letters
     - Inclusion of digits
     - Use of special characters
   - Categorizes passwords as:
     - `Very Weak`
     - `Weak`
     - `Strong`
     - `Very Strong`

2. **Secure Password Generator**
   - Generates strong, random passwords based on user-defined length (minimum 8 characters).
   - Uses a mix of:
     - Uppercase letters
     - Lowercase letters
     - Numbers
     - Special characters

3. **Brute-Force Time Estimator**
   - Calculates the estimated time to brute-force a password based on its complexity.
   - Assumes a brute-force rate of 1 billion attempts per second.

---

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/password-utility-tool.git
   cd password-utility-tool
   python main.py

