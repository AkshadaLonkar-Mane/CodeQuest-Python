
my_string = "Hello World 2024! python is fun."


# SOlution:


Exercise: 1
# Given the code below, insert the correct negative index to get the last character in the string.
"""
To get the last character of the string, we use negative indexing.
In Python, -1 refers to the last character, -2 refers to the second last, and so on.
"""
last_character = my_string[-1]
print(f"The last character of the string is: '{last_character}'")

# Output : The last character of the string is: '.'
#----------------------------------------------------------------


Exercise: 2
# Given the code below, insert the correct negative index to return the '!' character from the string.
"""
To get the  "!" charachter using negative indexing , we need to determine its position from the end.
The "!" charachter is the 18th position from the end.
"""
exclamation_mark =  my_string[-16]
print(f"The '!' charachter in the string is: '{exclamation_mark}'")

# Output:   The '!' charachter in the string is: '!' 
#----------------------------------------------------------------------



Exercise: 3
#Given the code below, insert the correct order to return the index of the "W" character in the string.
"""
The .index() method is used to find the first occurrence of a specified value.
In this case, we are looking for the character "W" in the string.
The index() method returns the index of the first occurrence of the substring if found.
If the substring is not found, it raises a ValueError.
"""

index_W = my_string.index("W")
print(f"The index of the 'W' character is: '{index_W}'")

# Output:  The index of the 'W' character is: '6' 
#----------------------------------------------------------------------


Exercise: 4
# Given the code below, insert the correct order to return the number of occurrences of the letter "o" in the string.
"""
The count() methd is used to find the total count of a specified value.
In this case, we are looking for the number of letter "o" in the string.
"""
Count_o = my_string.count("o")
print(f"The number of occurences of the letter 'o' is: '{Count_o}'")

# Output: The number of occurences of the letter 'o' is: '3'
#----------------------------------------------------------------------


Exercise: 5
# Given the code below, insert the correct order to convert all letters in the string to uppercase.
"""
The upper() method is used convert all letters in the string to uppercase.
"""
upper = my_string.upper()
print(f"Convert all letters in the string to uppercase: '{upper}'")

# Output: Convert all letters in the string to uppercase: 'HELLO WORLD 2024! PYHTON IS FUN.'
#----------------------------------------------------------------------------------------------


Exercise: 6
# Given the code below, insert the correct order to get the index at which the substring "python" starts.
"""
To find the starting index of the substring "python", we use the .find() method.
The .find() method returns the lowest index at which the substring is found in the string.
If the substring is not found, it returns -1.
"""
index_python = my_string.find("python")
print(f"The index where the substring 'python' starts is: '{index_python}'")

# Output: The index where the substring 'python' starts is: '18'
#-------------------------------------------------------------------------------------------------------

Exercise: 7
# Given the code below, insert the correct order to check of the string starts with the letter H.
"""
To find string is start with letter H, we are going to use startswith() method.
"""
if my_string.startswith("H"):
    print("The string starts with letter 'H'.")
else:
    print("The string NOT starts with letter 'H'.")

# Output: The string starts with letter 'H'.
#----------------------------------------------------------------------------------------------

Exercise: 8
# Given the code below, insert the correct order to convert all uppercase letters to lowercase and all lowercase letters to uppercase.
"""
The swapcase() method converts all uppercase letters to lowercase and all lowercase letters to uppercase in the string.
# """
swap_string = my_string.swapcase()
print("swap string is : ", swap_string)

# Output: swap string is :  hELLO wORLD 2024! PYTHON IS FUN.
#----------------------------------------------------------------------------------------------


Exercise: 9
# Given the code below, insert the correct  order to remove all spaces (single Space characters from the keyboard) from the string.
"""
To remove all spaces (single Space characters from the keyboard) from the string, we use the replace() method 
"""
no_space_string = my_string.replace(' ', '')
print("no_space_string is : ", no_space_string)

# Output: swap string is : no_space_string is :  HelloWorld2024!pythonisfun. 
#----------------------------------------------------------------------------------------------


Exercise: 10
# Given the code below, insert the correct order to replace all the occurrences of letter 'o' with the substring '123'.
"""
To replace all 'o' with '123', we use the replace() method.
"""

modified_string = my_string.replace("o", "123")

# Print the resulting string with the replacements
print("modified string is : ", modified_string)

# Output: modified string is :  Hell123 W123rld 2024! pyth123n is fun.
#----------------------------------------------------------------------------------------------

Exercise: 11
# Given the code below, insert the correct order to split the entire string in two parts, using the '!' as a delimiter.
"""
To split the entire string in two parts, we are using split() method
"""
split_string = my_string.split("!")
print('split string is: ', split_string)

# Output: split string is:  ['Hello World 2024', ' python is fun.']
#----------------------------------------------------------------------------------------------


Exercise: 12
# Given the code below, insert the correct order to join the characters of the string using the '-' symbol as a delimiter.
""" 
To join the character of the string using '-' symbol, we are using join() method.
"""
join_string = "-".join(my_string)
print('join string using - is: ', join_string)

# Output: join string using - is:  H-e-l-l-o- -W-o-r-l-d- -2-0-2-4-!- -p-y-t-h-o-n- -i-s- -f-u-n-.
#----------------------------------------------------------------------------------------------

Exercise: 13
# Given the code below, insert the correct order to concatenate my_string with the following string:
my_other_string = "Welcome to my Code Quest!"
"""

"""
my_other_string = "Welcome to my Code Quest!"
new_string = my_string + " "+ my_other_string
print("my new string is : ", new_string)

# Output:
""" my new string is :  Hello World 2024! python is fun. Welcome to my Code Quest!"""
#----------------------------------------------------------------------------------------------

Exercise: 14
# Given the code below, insert the correct order to convert the first letter of each word in the string to uppercase.
"""
To convert the fist letter of each word in the string to uppercase, we using titile() method.
"""
string_title = my_string.title()
print("Uppercase title is: ", string_title)

# Output: Hello World 2024! Python Is Fun.
#----------------------------------------------------------------------------------------------



