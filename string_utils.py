 
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def is_palindrome(s):
    reversed_s = reverse_string(s)
    return s == reversed_s
