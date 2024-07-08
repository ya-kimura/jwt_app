# utils.py
import math
import re

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = math.isqrt(num)
    for d in range(3, max_divisor + 1, 2):
        if num % d == 0:
            return False
    return True

def is_valid_name(name):
    return bool(re.match(r'^[^\d]{1,256}$', name))

def is_valid_role(role):
    return role in ['Admin', 'Member', 'External']
