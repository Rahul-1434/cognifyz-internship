def is_palindrome(s):
    reverse=s[::-1]
    if reverse==s:
        return True
    else:
        return False
    
string=input('Enter a string:')
if is_palindrome(string):
    print(f'{string} is a palindrome.')
else:
    print(f'{string} is not a palindrome.')