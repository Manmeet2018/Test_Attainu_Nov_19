# VST 4, November 15
# Question:

# Question no 1
# Write a Python function named largest that takes two number parameters (arguments) a and b returns the larges among those.

# Example:

# largest(10, 15) # Returns 15

# Question no 2
# Write a Python function named sum_of_array that takes an array (list) called arr as an argument and returns the sum of all elements in the array.

# Example:

# sum_of_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Returns 55

# Question no 3
# Write a Python function named print_even that takes an array (list) called arr as an argument and only prints even number in the list.

# Example:

# print_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Prints 2, 4, 6, 8, 10

# Note:
# Please use a text editor on your system or an online editor like http://repl.it to test your solution and copy paste your code here. You cannot test/run your code here.
# 2. It is recommended to submit all solutions together in the below editor.

# 3. You dont need to take inputs from the user or provide function calls. Just the function and the logic are enough.

# 4. Submissions after 1pm are considered invalid.

# 5. Even if you can only solve one or two question, please submit the answers for them. It is not required that you need to provide solution for all the three questions.

# 6. Please ask questions to your instructor on slack, if you have any.

# Solution 
# Question 1:

def largest(a,b):
	if(a>b):
		print(a)
	else:
		print(b)

# largest(5, 10) 

# Question 2:

def sum_of_array(arr):
  sum =0
  for i in arr:
    sum += i
  print(sum)
 # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 # sum_of_array(arr)

# Question 3:

def print_even(arr):
  for i in arr:
    if((i&1)==0):
      print(i)
      
 # print_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
