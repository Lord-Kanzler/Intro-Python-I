# Write a function is_even that will return true if the passed-in number
# is even.

# YOUR CODE HERE
def is_even(number):
    if number % 2 == 0:
        return "TRUE"

    else:
        return "FALSE"


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
print("Even!" if is_even(num) == "TRUE" else "Odd")
