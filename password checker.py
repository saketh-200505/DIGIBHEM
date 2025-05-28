import re

def check_password_complexity(password):
    length_criteria = len(password) >= 9
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    complexity_score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    if complexity_score == 5:
        return "Strong Password"
    elif complexity_score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

password = input("Enter your password: ")
print(check_password_complexity(password))
