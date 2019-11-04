#1 How do you swap two integers without using a temporary variable?
x = 10
y = 5
x = x + y
y = x - y
x = x - y
print("After Swapping: x =", x, " y =", y)

print("----------")

#2 Check if array/list is Palindrome
# Create a function
def isPalindrome(arr):
  # Create for loop with range() starting from 0, iterating through the length of array, then divide it by two.
  for i in range(0, int(len(arr) / 2)):
    # If arr[position i] doesn't equal array length substracted by 1, substracted by i.
    if arr[i] != arr[len(arr) - 1 - i]:
      # Then return false.
      return False
    # If the conditions don't apply, reply true.
    return True
# Create test array
testarray = [1,2,3,4,4,3,2,1]
# Print out array
print(isPalindrome(testarray))

print("----------")

#2.1 Another way of solving a Palindrome
# function which return reverse of a string 
def reverse(s): 
  return s[::-1] 
def isPalindromeTwo(s): 
  # Calling reverse function 
  rev = reverse(s)   
  # Checking if both string are equal or not 
  if (s == rev): 
    return True
  return False
s = "kayak"
ans = isPalindromeTwo(s) 
if ans == 1: 
  print("Yes") 
else: 
  print("No")

print("----------")

#2.2 Third way of solving Palindrome
def isPalindromeThree(s): 
  # Using predefined function to  
  # reverse to string print(s) 
  rev = ''.join(reversed(s)) 
  # Checking if both string are  
  # equal or not 
  if (s == rev): 
    return True
  return False
# main function 
s = "level"
ans = isPalindromeThree(s) 
if (ans): 
  print("Yes") 
else: 
  print("No")

print("----------")
