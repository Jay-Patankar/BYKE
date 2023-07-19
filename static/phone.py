import phonenumbers
x = phonenumbers.parse("+109909", None)
print(phonenumbers.is_possible_number(x))
print(phonenumbers.is_valid_number(x))
