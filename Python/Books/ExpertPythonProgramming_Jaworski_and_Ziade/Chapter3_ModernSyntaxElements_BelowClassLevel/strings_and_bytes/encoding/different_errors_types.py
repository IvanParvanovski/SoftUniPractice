my_name = 'Ivan Parvanovski ☢'

# encode_error_strict = my_name.encode('ascii', 'strict')
encode_error_ignore = my_name.encode('ascii', 'ignore')
encode_error_replace = my_name.encode('ascii', 'replace')
encode_error_xmlcharrefreplace = my_name.encode('ascii', 'xmlcharrefreplace')

# print(encode_error_strict)
print(encode_error_ignore)
print(encode_error_replace)
print(encode_error_xmlcharrefreplace)
