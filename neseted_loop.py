rows = int(input("Please enter the number of rows here! "))
columns = int(input("Please enter the number of columns here "))
symbol = input("Please select the symbol here ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()