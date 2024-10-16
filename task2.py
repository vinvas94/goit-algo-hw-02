from collections import deque

def is_palindrome(value):
    # Normalize the string: lower case and remove spaces
    normalized_string = ''.join(ch.lower() for ch in value if ch.isalnum())
    char_deque = deque(normalized_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

print(is_palindrome("Hello"))
print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("1258521")) 
print(is_palindrome("125849754")) 




