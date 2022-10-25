from cs50 import get_int

while (True):
    height = get_int("Height: ")
    if(height > 0 and height <= 8):
        break
    else:
        print("Height should be a positive integer but not greater than 8.")

for i in range(height):
    for j in range(height-1, i-1, -1):
        if (i == j):
            print("#" * (i+1), end="")
        else:
            print(" ", end="")

    print("  ", end="")

    for k in range(height):
        if (i == k):
            print("#" * (i+1), end="")
            continue
    print()