# Literals
def literals():
    """
    --- Definition ---
    Very big or very small float numbers

    --- Input ---
    8.8 ** -5.4

    --- Output ---
    Output = 7.939507629591553e-06

    """

    print(8.8 ** 5.4)


# Overflow error
def overflow_error():
    """
    --- Definition ---
    Calculation with floating point / number
    which was very big or very small

    --- Input ---
    500.0 ** 1000

    --- Output ---
    OverflowError

    Output =

        Traceback (most recent call last):
    File "C:/Users/iparv/Desktop/SoftUni/Python/Sofia_University_Book_Practice/test.py", line 20, in <module>
        overflow_error()
    File "C:/Users/iparv/Desktop/SoftUni/Python/Sofia_University_Book_Practice/test.py", line 18, in overflow_error
        print(500.0 ** 1000)
    OverflowError: (34, 'Result too large')
    """

    print(500.0 ** 1000)


# Complex numbers
def complex_numbers():
    """
       --- Definition ---
       Negative number under the square root

       --- Input ---
       1j * 1j

       --- Output ---
       Output = (-1+0j)

       """

    print(1j * 1j)


# String concatenation
def concatenation():
    """
    --- Definition ---
    Incorporation(Sum) of different strings into one big

    --- Input ---
    first_part = "Hello "
    second_part = "Brian"
    final_part = "!"

    message = first_part + second_part + final_part <- concatenation
    --- Output ---
    Output = "Hello Brian!"

    """
    first_part = "Hello "
    second_part = "Brian"
    final_part = "!"

    message = first_part + second_part + final_part
    print(message)



concatenation()