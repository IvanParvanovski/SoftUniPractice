user_string_input = input().split()
factor = int(input())
numbers = list(int(element) * factor for element in user_string_input)


def output():
    output_concatenation = f"Score: {happy_counter}/{len(numbers)}. Employees are "
    if happy_counter >= len(numbers) / 2:
        output_concatenation += "happy!"
    else:
        output_concatenation += "not happy!"
    return output_concatenation


def calculate_average():
    return sum(numbers) / len(numbers)


happy_counter = sum(list(1 for num in numbers if num >= calculate_average()))
average = calculate_average
print(output())
