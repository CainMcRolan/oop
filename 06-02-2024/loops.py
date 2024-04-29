#Write a Python program that will display the following output. 
#For Loops Activity 2
a=0
b=0
c=0

for i in range(1, 8):
    for j in range(1, (7-i)+1):
        print("  ", end="")
        a+=1
    
    while c != ((2*i)-1):
        if a<=7-1:
            print(c + 1, end=" ")
            a+=1
        else:
            b+=1
            print(c + 1 -(2*b), end=" ")
        c += 1
    
    a,b,c = 0, 0, 0
    print()
    
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ",end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart(n)


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart2(n):
	
	# number of spaces
	k = 2*n - 2

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 2
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart2(n)

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)

        # * * * * * * 
        #  * * * * * 
        #   * * * * 
        #    * * * 
        #     * * 
        #      *

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
    
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
    
#hollow box
rows = int(input("Enter Number of Rows: "))
columns = int(input("Enter Number of Columns: "))
print("Hollow Box Pattern with", rows, "rows and", columns,"columns")
 
for i in range(0, rows):
    for j in range(0, columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('1', end = '  ')
        else:
            print(' ', end = '  ')
    print()

#right triangle
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

#sandglass
rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

# def pattern(n):
#      k = n - 2
#      for i in range(n, -1 , -1):
#           for j in range(k , 0 , -1):
#                print(end=" ")
#           k = k + 1    
#           for j in range(0, i+1):
#                print("* " , end="")
#           print("&#92r")
#       k = 2 * n  - 2
#       for i in range(0 , n+1):
#            for j in range(0 , k):
#                print(end="")
#            k = k - 1
#             for j in range(0, i + 1):
#                  print("* ", end="")
#             print("&#92r")
 
# pattern(5)

#diamond
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
#hollow diamond
rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1
	