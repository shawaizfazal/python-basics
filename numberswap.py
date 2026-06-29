

# Step 1: Asking for the 3 numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

print("\n Before Swapping")
print("a =", a, ", b =", b, ", c =", c)

# Step 2x Doing the magic swap using a temporary variable
temp = a   # Save a in temp
a = b      # Put b into a
b = c      # Put c into b
c = temp   # Put the saved a (from temp) into c

# Step 3: Showing the final results
print("\n AfterSwapping ")
print("Yay the numbers are swapped")
print("a =", a, ", b =", b, ", c =", c)