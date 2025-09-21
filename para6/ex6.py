class NumberError(Exception):
    def __str__(self):
        return f"First number < second number"


def check_number(num1, num2):
    if num1 > num2:
        try:
            res = num1 / num2
        except ZeroDivisionError:
            res = "0 div!"
        print(res)
    else:
        raise NumberError
n1 = float(input("Enter num1: "))
n2 = float(input("Enter num2: "))
check_number(n1,n2)