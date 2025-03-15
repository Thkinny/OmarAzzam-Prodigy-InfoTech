import string

def assess_password_strength(password):
    upper_case = any(c in string.ascii_uppercase for c in password)
    lower_case = any(c in string.ascii_lowercase for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c in string.digits for c in password)

    characters = [upper_case, lower_case, special, digits]
    characterPoints = sum(characters)
    length = len(password)

    score = 0

    with open('password-list.txt', 'r') as f:
        Common = f.read().splitlines()

    if password in Common:
        print("Password was found in common list. Score 0/7")
        return

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    print(f"Password length is {length}, adding {score} points!")

    if characterPoints > 1:
        score += 1
    if characterPoints > 2:
        score += 1
    if characterPoints > 3:
        score += 1

    print(f"Password has {characterPoints} different character types, adding {characterPoints} points!")

    if score < 4:
        print(f"The password is weak! Score: {score}/7")
    elif score == 4:
        print(f"The password is ok! Score: {score}/7")
    elif 4 < score < 6:
        print(f"The password is pretty good! Score: {score}/7")
    elif score >= 6:
        print(f"The password is strong! Score: {score}/7")


password = "tdsSGDsdSDCV@#SDF"
assess_password_strength(password)