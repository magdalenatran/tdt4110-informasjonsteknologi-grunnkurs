def check_equal(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

def reversed_word(str):
    reversed = ''
    for i in range(1, len(str)+1):
        reversed += str[len(str) - i]
        print(reversed)
    return reversed

def check_palindrome(str):
    reversedstr = reversed_word(str)
    if str == reversedstr:
        return True
    else:
        return False

def contains_string(str1, str2):
    position = str1.find(str2)
    return position


str1 = 'hei'
str2 = 'hello'
str3 = 'hello'

print(check_equal(str1, str2))
print(check_equal(str3, str2))

str = 'Morna Jens'
print(reversed_word(str))

str1 = 'agnes i senga'
str2 = 'hello'
print(check_palindrome(str1))
print(check_palindrome(str2))

str1 = 'pepperkake'
str2 = 'per'
str3 = 'ola'
print(contains_string(str1, str2))
print(contains_string(str1, str3))
