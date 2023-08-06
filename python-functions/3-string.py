def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string
reverse_string = __import__('3-string').reverse_string

print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))