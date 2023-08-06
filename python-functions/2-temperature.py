def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
convert_to_celsius = __import__('2-temperature').convert_to_celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))