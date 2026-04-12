try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
# Output: Error: Denominator cannot be 0.

# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)


try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
finally:
    print("This is finally block.")


# define Python user-defined exceptions
#class InvalidAgeException(Exception):
 #   "Raised when the input value is less than 18"
 #   pass
# you need to guess this number
#number = 18

#try:
  #  input_num = int(input("Enter a number: "))
 #   if input_num < number:
  #      raise InvalidAgeException
 #   else:

 #   print("Eligible to Vote")
#except InvalidAgeException:
  # print("Exception occurred: Invalid Age")