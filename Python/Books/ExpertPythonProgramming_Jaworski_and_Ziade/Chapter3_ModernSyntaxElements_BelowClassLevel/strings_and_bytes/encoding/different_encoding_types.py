my_name = 'Ivan Parvanovski ☢'

encoded_name_utf8 = my_name.encode('utf-8', 'strict')
encoded_name_utf16 = my_name.encode('utf-16', 'strict')
encoded_name_utf32 = my_name.encode('utf-32', 'strict')

print(my_name.encode('utf-8'))
print(encoded_name_utf8)
print(encoded_name_utf32)
print(bytes(my_name, 'utf-8', 'strict'))
