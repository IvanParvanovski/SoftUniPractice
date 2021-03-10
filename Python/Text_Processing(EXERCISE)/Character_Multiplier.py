user_input = input().split()
first_str = user_input[0]
second_str = user_input[1]
bigger_str = ""
smaller_str = ""
sum = 0
if len(second_str) > len(first_str):
    bigger_str = second_str
    smaller_str = first_str
else:
    bigger_str = first_str
    smaller_str = second_str

for index in range(len(bigger_str)):
    first_char = 0
    second_char = 0
    if index >= len(smaller_str):
        if smaller_str == first_str:
            second_char = ord(second_str[index])
        else:
            first_char = ord(first_str[index])
        sum += first_char + second_char
    else:
        second_char = ord(second_str[index])
        first_char = ord(first_str[index])
        sum += first_char * second_char

print(sum)