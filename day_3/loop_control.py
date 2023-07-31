#The loop control statement are used to change a loop execution from it's normal sequence
#They are : break, continue and pass

# Continue skips to the next iteration
#Break terminates the loop entirel
#Pass does nothing. It just acts as a placeholder

# numbers = [2,2,2,2,8]
# for i in numbers:
#     print("*" * i)

secret_number = 9
while True:
    user = int(input("Please enter a number from 0-9  "))
    if user == secret_number:
        print("You won")
        break



phone_number = ("123-456-7890")
for i in  phone_number:
    if i == "-":
        pass
    else:
        print(i)




for i in range(1,100):
    if i % 2 == 0:
        print(i)


for i in range(20,50):
    if i % 3 != 0:
        print(i)



for i in range(10,20):
    if i % 2 == 0:
        print(i , "Is an even number")