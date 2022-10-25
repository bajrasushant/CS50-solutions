from cs50 import get_int
import re

number = get_int("Number: ")
sum = 0

for i in range(len(str(number))-1, -1, -2):
    n = 2 * int(str(number)[i-1])
    if (n > 10):
        while n != 0:
            rem = n % 10
            sum = sum + rem
            n = n // 10
    else:
        sum = sum + n


if (sum % 10 == 0):
    str_number = str(number);
    if (str_number.startswith("37") or str_number.startswith("34")):
        print("AMEX")
    elif (re.search("^[5][1-5]", str_number)):
        print("MASTERCARD")
    elif (re.search("^4"), str_number):
        print("VISA")
else:
    print("INVALID")