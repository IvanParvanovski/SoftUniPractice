def input_and_operation():
    num = int(input())

    if num < 100:
        main_string = percent_call(num) + bar(num)
        print(main_string)
        print(text_call(num))
    if num == 100:
        main_string = percent_call(num) + text_call(num)
        print(main_string)
        print(bar(num))


def bar(num):
    bar_string = "["
    for counter in range(int(num / 10)):
        bar_string += "%"
    for counter in range(10 - int(num / 10)):
        bar_string += "."
    bar_string += "]"
    return bar_string


def percent_call(num):
    string_percent = str(num) + "% "
    return string_percent


def text_call(num):
    string = ""
    if num < 100:
        string = "Still loading..."
    if num == 100:
        string = "Complete!"
    return string


input_and_operation()