# ------------------------------ Encoding ------------------------------


encode_way1 = 'hello'.encode(encoding='utf-8',
                             errors='ignore')

encode_way2 = bytes('hello',
                    encoding='utf-8',
                    errors='ignore')

print(encode_way1)
print(encode_way2)


encode_way3 = 'hello'.encode()
encode_way4 = bytes('hello',
                    encoding='utf-8')


print(encode_way3)
print(encode_way4)


# ------------------------------ Decoding ------------------------------

my_byte_array = bytes([111, 122, 111])

decode_way1 = my_byte_array.decode(encoding='utf-8',
                                   errors='strict')

decode_way2 = str(my_byte_array,
                  encoding='utf-8',
                  errors='strict')

print(decode_way1)
print(decode_way2)

decode_way3 = my_byte_array.decode()
decode_way4 = str(my_byte_array,
                  encoding='utf-8',)

print(decode_way3)
print(decode_way4)
