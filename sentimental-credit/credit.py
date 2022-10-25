# from cs50 import get_int
# import re

# number = get_int("Number: ")
# sum = 0

# for i in range(len(str(number))-1, -1, -2):
#     n = 2 * int(str(number)[i-1])
#     if (n > 10):
#         while n != 0:
#             rem = n % 10
#             sum = sum + rem
#             n = n // 10
#     else:
#         sum = sum + n


# if (sum % 10 == 0):
#     str_number = str(number);
#     if (str_number.startswith("37") or str_number.startswith("34")):
#         print("AMEX")
#     elif (re.search("^[5][1-5]", str_number)):
#         print("MASTERCARD")
#     elif (re.search("^4"), str_number):
#         print("VISA")
# else:
#     print("INVALID")

from cs50 import get_int
from re import search

number = get_int("Number: ")
str_number = str(number)

sum = 0
for i in range(len(str_number)-1, -1, -2):
    print(i)
    n = 2 * int(str_number[i-1])
    print(n)
    if (n > 10):
        while n != 0:
            rem = n % 10
            n = n // 10
            sum = sum + rem
            print(sum)
    else:
        sum = sum + n
print(sum)
if (sum % 10 == 0):
    if (re.search("^37"|"^34", str_number)):
        print("AMEX")
    else:
        print("VALID BUT INVALID")
else:
    print("INVALID")
