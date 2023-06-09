from cs50 import get_int
import re

number = get_int("Number: ")
str_number = str(number)

sum = 0

# second last characters step - 2
for i in range(len(str_number)-2, -1, -2):
    # len - 2 as if length is 15 then we need the 13th element of the array(second last)
    n = 2 * int(str_number[i])

    if (n >= 10):
        while n != 0:
            rem = n % 10
            n = n // 10
            sum = sum + rem
    else:
        sum = sum + n

# remaining elements
for i in range(len(str_number)-1, -1, -2):
    sum = sum + int(str_number[i])
# checking
if (sum % 10 == 0):
    if (re.search("^34|^37", str_number) and len(str_number) == 15):
        print("AMEX")
    elif (re.search("^[5][1-5]", str_number) and len(str_number) == 16):
        print("MASTERCARD")
    elif (re.search("^4", str_number) and (len(str_number) == 13 or len(str_number) == 16)):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")