import re

def check_password_strength(password):
    # Define strength levels
    score = 0
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Evaluate the password against criteria
    if length_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if special_criteria:
        score += 1

    # Assess the strength based on score
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# Prompt user for input
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"The password strength is: {strength}")
