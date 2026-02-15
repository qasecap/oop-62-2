def check_password(password):
    if len(password) < 6:
        return False

    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False

    for char in password:
        if char.isdigit(): has_digit = True
        if char.isupper(): has_upper = True
        if char.islower(): has_lower = True
        if not char.isalnum(): has_special = True
    return has_digit and has_upper and has_lower and has_special

def nearest_number(numbers, target=0):
    res = numbers[0]
    for n in numbers:
        if abs(n - target) < abs(res - target):
            res = n
    return res

print(nearest_number([1, 2, 3], 5))

