# Numbers Booleans Solutions:

Exercise: 1
# Convert the number 45 into a float
num = 45
float = float(num)
print(float)

# Output : 45.0
#----------------------------------------------------------------


Exercise: 2
#convert 13.76 into integer number
num = 13.76
int = int(num)
print(int)
# Output : 13
#----------------------------------------------------------------


Exercise: 3
# calculate the remainder when 60 is divided by 7
remainder = 60 % 7
print("reminder = " , remainder)

# Check if the remainder is equal to 1
is_equal_to_one = (remainder == 1)
print("Is the remainder equal to 1?", is_equal_to_one) 

# Output :
"""
reminder =  4
Is the remainder equal to 1? False
"""
#----------------------------------------------------------------


Exercise: 4
# calculate 10 raised to the power of 3.
result = 10 ** 3
print("10 raised to the power of 3 = ", result)

# Output : 10 raised to the power of 3 =  1000 
#----------------------------------------------------------------


Exercise: 5
# integer division of 45 by 7
result = 45 // 7
print("integer division of 45 by 7 = ", result )

# Output : integer division of 45 by 7 =  6
#----------------------------------------------------------------


Exercise: 6
# find the absolute value of -34
result = abs(-34)
print("Absolute value of -34 = ", result)

# Output : Absolute value of -34 =  34
#----------------------------------------------------------------


Exercise: 7
# Calculate 20 raised to the power of 5 using the pow() function
result = pow(20, 5)
print("20 raised to the power of 5 is:", result) 

# Output : 20 raised to the power of 5 is: 3200000
#----------------------------------------------------------------


Exercise: 8
# Define the conditions
a = ((25 % 7 + 10 / 2) % 3 == 0)
b = ((abs(-19) / 2 - 2) > 9)

# Use a logical operator to combine the conditions so that the result is False
result = a and b

print("The result of combining a and b is:", result)  

# Output : The result of combining a and b is: False
#----------------------------------------------------------------


Exercise: 9
# Define the conditions
a = ((25 % 7 + 10 / 2) % 3 == 0)
b = ((abs(-19) / 2 - 2) > 9)

# Use a logical operator to combine the conditions so that the result is True
result = a or b

print("The result of combining a and b is:", result)  

# Output : The result of combining a and b is: True
#----------------------------------------------------------------


Exercise: 10
# Compute the arithmetic expression
result = (15 * 4 + 20) / 5

# Check if the result is greater than 100
is_greater_than_100 = result > 100

print("result = ", result)
print("Is the result greater than 100?", is_greater_than_100)  

# Output : 
"""
result =  16.0
Is the result greater than 100? False
"""
#----------------------------------------------------------------


Exercise: 11
# check if the number 75 is less than 100 and greater than 50. Print the result.

# Check if the result is less than 100 and greater than 50
compare_num  = 50 < 75 < 100
print("number 75 is less than 100 and greater than 50 ?", compare_num)

# Output : number 75 is less than 100 and greater than 50 ? True
#----------------------------------------------------------------


Exercise: 12
# check if num is either greater than 10 or less than 5. Set num to 8

compare_num = (num > 5) or (num < 10)
num = 8
print("num is either greater than 10 or less than 5? ", compare_num)

# Output : num is either greater than 10 or less than 5?  True
#----------------------------------------------------------------


Exercise: 13
# Check if 25 is not equal to 30 and print the result after applying the not operator.
compare_num = (25 != 30)
print("Check if 25 is not equal to 30?  ", compare_num)

# Output : Check if 25 is not equal to 30?   True
#----------------------------------------------------------------


Exercise: 14
# compare if 0.6 + 0.2 is equal to 0.8
print("0.6 + 0.2 is equal to 0.8 ?  ",0.6 + 0.2 == 0.8 )

# Output : 0.6 + 0.2 is equal to 0.8 ? True
#----------------------------------------------------------------


Exercise: 15
# division of 29 by 4, then check if the result is greater than 5.
div = 29 /4
result = div > 5

print("div =", div, "\nIs  division greater than 5?", result)

# Output : 
"""
div = 7.25
Is  division greater than 5? True
"""
#----------------------------------------------------------------


Exercise: 16
# Integer division of 29 by 4, then check if the result is greater than 5.
int_div = 29 //4
result = int_div > 5

print("int_div =", int_div, "\nIs integer division greater than 5?", result)
# Output :
"""
int_div = 7
Is integer division greater than 5? True
"""
#----------------------------------------------------------------


Exercise: 17
# Calculate the modulus of 17 divided by 5
result = 17 % 5
is_equal_to_2 = (result == 2)

print("result = " , result, "\nThe modulus of 17 divided by 5 is equal to 2:", is_equal_to_2)  

# Output : 
"""
result =  2
The modulus of 17 divided by 5 is equal to 2: True
"""
#----------------------------------------------------------------


Exercise: 18
# check if num is between 10 and 20, inclusive. Set num to 15.

is_num_between_10and20 = 10 < num< 20
num = 15
print('num is between 10 and 20 ? ', is_num_between_10and20)

# Output : num is between 10 and 20 ?  False
#----------------------------------------------------------------


Exercise: 19
# check if number is even or odd. Set number to 42

number = 42

# Boolean variable to check if the number is even
is_even = (number % 2 == 0)

if is_even:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Output : 42 is even.
#----------------------------------------------------------------


Exercise: 20
"""calculate the absolute difference between num1 and num2 and check if it is less than 10. 
Set num1 to 25 and num2 to 18."""

num1 = 25
num2 = 18

# Calculate the absolute difference
difference = abs(num1 - num2)

# Boolean variable to check if the difference is less than 10
is_less_than_10 = (difference < 10)

print(f"The absolute difference between {num1} and {num2} is {difference}.")
if is_less_than_10:
    print("The difference is less than 10.")
else:
    print("The difference is not less than 10.")

# Output : 
"""
The absolute difference between 25 and 18 is 7.
The difference is less than 10.
"""
#----------------------------------------------------------------



Exercise: 21
# Calculate 2 raised to the power of 5
result = 2 ** 5

# Boolean variable to check if the result is greater than 30
is_greater_than_30 = (result > 30)

print(f"2 raised to the power of 5 is {result}.")
if is_greater_than_30:
    print("The result is greater than 30.")
else:
    print("The result is not greater than 30.")

# Output : 
"""
2 raised to the power of 5 is 32.
The result is greater than 30.
"""
#----------------------------------------------------------------
Exercise: 22
# Calculate 0.5 * 0.5
result = 0.5 * 0.5

# Boolean variable to check if the result is equal to 0.25
is_equal_to_025 = (result == 0.25)

print(f"0.5 * 0.5 is {result}.")
if is_equal_to_025:
    print("The result is equal to 0.25.")
else:
    print("The result is not equal to 0.25.")

# Output :
"""
0.5 * 0.5 is 0.25.
The result is equal to 0.25.
"""
#----------------------------------------------------------------


Exercise: 23
# Check if 10 is not equal to 20
is_not_equal = (10 != 20)

# Apply the not operator
result = not is_not_equal


print(f"10 is not equal to 20: {is_not_equal}")
print(f"Applying the 'not' operator gives: {result}")

# Output : 
"""
10 is not equal to 20: True
Applying the 'not' operator gives: False
"""
#----------------------------------------------------------------


Exercise: 24
# Compute the expression 5 + 10 * 2
result = 5 + 10 * 2

# Boolean variable to check if the result is less than 30
is_less_than_30 = (result < 30)

print(f"The result of 5 + 10 * 2 is {result}.")
if is_less_than_30:
    print("The result is less than 30.")
else:
    print("The result is not less than 30.")

# Output : The result is greater than 30.

#----------------------------------------------------------------
Exercise: 25
# Compute 100 % 7
remainder = 100 % 7

# Boolean variable to check if the remainder is less than 5
is_less_than_5 = (remainder < 5)

# Print the remainder and whether it is less than 5
print(f"The remainder of 100 % 7 is {remainder}.")
if is_less_than_5:
    print("The remainder is less than 5.")
else:
    print("The remainder is not less than 5.")

# Output : 
"""
The remainder of 100 % 7 is 2.
The remainder is less than 5.
"""
#----------------------------------------------------------------
