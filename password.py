print("Password strength evaluation complete.")password = input("Enter your password: ")
length = len(password)
score = 0
if length >= 8:
    score += 1
    print("Your password is strong enough.")
else:
    print("Your password is not strong enough.")
has_upper = False
has_lower = False
has_digit = False
has_special = False
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1
print("Password contains uppercase letter:", has_upper)
print("Password contains lowercase letter:", has_lower)
print("Password contains digit:", has_digit)
print("Password contains special character:", has_special)
print("Password strength score:", score)
if score >= 4:
    print("Your password is very strong.")
elif score == 3:
    print("Your password is strong.")
elif score == 2:
    print("Your password is moderate.")
elif score == 1:
    print("Your password is weak.")
else:
    print("Your password is very weak.")

print("Password strength evaluation complete.")
