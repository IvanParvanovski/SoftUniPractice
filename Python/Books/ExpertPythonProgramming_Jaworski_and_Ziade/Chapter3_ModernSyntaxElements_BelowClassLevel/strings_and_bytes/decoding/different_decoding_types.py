my_name = b'Ivan Parvanovski \xe2\x98\xa2'

decoded_name_utf8 = my_name.decode('utf-8', 'strict')
decoded_name_utf16 = my_name.decode('utf-16', 'strict')

print(decoded_name_utf8)
print(decoded_name_utf16)
print(my_name.decode('utf-8'))
