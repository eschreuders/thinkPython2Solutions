from __future__ import print_function, division


def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) > 1:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return False
    else:
        return True


print(first("birthday"), last("birthday"), middle("birthday"))
#print(first("egg"), last("egg"), middle("egg"))
#print(first("al"), last("al"), middle("al"))
print(first("e"), last("e"), middle("e"))
#print(first(""), last(""), middle(""))

print("catsuit", is_palindrome("catsuit"))

print("egg", is_palindrome("egg"))

print("noon", is_palindrome("noon"))

print("redivider", is_palindrome("redivider"))

print("", is_palindrome(""))



