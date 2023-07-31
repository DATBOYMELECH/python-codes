# numbers = [2,2,2,2,8]


# for i in numbers:
#     print( "*" * i)
# print()

# numbers = [8,2,2,8,2,2]
# for i in numbers:
#     print("*" * i)

# print()

# numbers = [8,2,2,8,2,8]
# for i in numbers:
#     print( "*" * i)
# print()




# numbers = [2,2,2,5,2,2,2]
# for i in numbers:
#     if i == 5:
#         continue
#     else: print("*"*i, "   ", "*"*i )




def print_pattern(n):
    # Outer for loop for number of rows
    for rows in range(n):
        # Inner for loop columns
        for columns in range(n):
            # prints first and last column
            if ((columns == 0 or columns == n-1) or
               # prints middle row
                (rows == n // 2)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
size = int(input("Enter size: \t"))
if size < 8:
    print("Enter a size greater than 8")
else:
    print_pattern(size)