password = input("Enter your password: ")

length = len(password)
score = 0

# Check password length
if length >= 8:
    score += 1
    print("Your password is strong enough.")
else:
    print("Your password is not strong enough.")

# Variables to check password characters
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

# Add points
if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

# Display character checks
print("Password contains uppercase letter:", has_upper)
print("Password contains lowercase letter:", has_lower)
print("Password contains digit:", has_digit)
print("Password contains special character:", has_special)

# Display score
print("Password strength score:", score)

# Evaluate password strength
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
