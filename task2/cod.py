4. PYTHON SOURCE CODEpython# Sum of digits of a number

num = int(input("Enter a number: "))
original = num
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    num = num // 10

print(f"Sum of digits of {original} is {sum_digits}")Alternate using for loop:pythonnum = input("Enter a number: ")
sum_digits = 0
for d in num:
    sum_digits += int(d)
print(f"Sum is {sum_digits}")5. SAMPLE INPUT 1javascriptEnter a number: 123SAMPLE OUTPUT 1javascriptSum of digits of 123 is 66. SAMPLE INPUT 2javascriptEnter a number: 4567
