password = input("Enter your password: ")
length = len(password)
score = 0
if length >= 8:
    score += 1
    print("Your password is strong.")
else:
    print("Your password is not strong enough.")
# Variable to check for uppercase letters
has_upper = None
has_lower = None
has_digit = None  
has_special = None
for char in password:
    if char.isupper():
        has_upper = Yes
    elif char.islower():
        has_lower = Yes
    elif char.isdigit():
        has_digit = Yes
    elif not char.isalnum():
        has_special = Yes
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
elif score == 0:
    print("Your password is very weak.")

print("Password strength evaluation complete.")