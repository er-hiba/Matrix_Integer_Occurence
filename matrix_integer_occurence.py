# This program prompts the user to input the dimensions of a matrix (rows and columns),
# fills the matrix with user-input integers, displays the matrix, and then asks the user
# to input an integer to search for within the matrix. It counts the occurrences of the
# specified integer within the matrix and displays the results based on the occurrences found.


# Prompt the user to input the number of rows and columns for the matrix
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

matrix = [[0 for _ in range(c)] for _ in range(r)]       # matrix initialized with zeros

# Fill the matrix by user-input integers
for i in range(r):
    for j in range(c):
        matrix[i][j] = int(input(f"Enter integer value at position [{i}][{j}]: "))

# Display the matrix
print(f"\nThe matrix {r}x{c}: ")
for row in matrix:
    print(row)

# Ask the user for an integer to search for in the matrix
n = int(input("\nWhat integer you want to find in the matrix: "))

# Initialize a counter for the occurences of the integer
counter = 0   

# Iterate through the matrix to find occurrences of the specified integer
for i in range(r):
    for j in range(c):
        if matrix[i][j] == n :         # Check if the current element matches the searched integer
            counter += 1               # Increment counter for each occurrence


# Display results based on the occurrences found
if counter > 0:
    print(f"\n{n} is in the matrix")
    print(f"The number of occurrences of {n} in the matrix is {counter}")
else:
    print(f"\n{n} is not in the matrix")
