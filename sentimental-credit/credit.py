from cs50 import get_int
import re

number = get_int("Number: ")
str_number = str(number)

sum = 0

#second last characters step - 2
for i in range(len(str_number)-2, -1, -2):
    n = 2 * int(str_number[i])
    if (n > 10):
        while n != 0:
            rem = n % 10
            n = n // 10
            sum = sum + rem
    else:
        sum = sum + n
    print(f"sum:{sum}")

for i in range(len(str_number)-1, -1, -2):
    sum = sum + int(str_number[i])
print(f"sum: {sum}")

if (sum % 10 == 0):
    if (re.search("^34|^37", str_number)):
        print("AMEX")
    else:
        print("VALID BUT INVALID")
else:
    print("INVALID")
