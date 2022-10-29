from cs50 import get_string
from re import search

user_input = get_string("Text: ")

words = 1
sentences = 0
letters = 0

for i in range(len(user_input)):
    if (user_input[i] == " " or user_input[i] == '\0'):
        words += 1
    elif (user_input[i] == "." or user_input[i] == "!" or user_input[i] == "?"):
        sentences += 1
    elif (search("[a-z]|[A-Z]", user_input[i])):
        letters += 1
# print(f"Letters: {letters}")
# print(f"WORDS: {words}")
# print(f"sentences: {sentences}")

lpw = (letters / words) * 100  # letters per 100 words
spw = (sentences / words) * 100  # sentences per 100 words

grade = (0.0588 * lpw) - (0.296 * spw) - 15.8
grade = round(grade)
if (grade >= 16):
    print("Grade: 16+")
elif (grade < 1):
    print("Before Grade 1")
else:
    print(f"Grade: {grade}")