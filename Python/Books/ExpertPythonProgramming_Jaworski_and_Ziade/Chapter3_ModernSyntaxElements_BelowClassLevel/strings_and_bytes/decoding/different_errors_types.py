my_name = b'Ivan Parvanovski \xe2\x98\xa2'

# decode_error_strict = my_name.decode('ascii', 'strict')
decode_error_ignore = my_name.decode('ascii', 'ignore')
decode_error_replace = my_name.decode('ascii', 'replace')
# decode_error_xmlcharrefreplace = my_name.decode('ascii', 'xmlcharrefreplace')

# print(decode_error_strict)
print(decode_error_ignore)
print(decode_error_replace)
# print(decode_error_xmlcharrefreplace)
