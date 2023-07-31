# count = 0
# while count < 9:
#     print("I am in a loop , please help me!!")
#     count = count + 1
# name = ""
# while len(name) == 0:
#     name = input("Please enter your email")
# print("Hello ", name)

# import time
# for second in range(10,0,-1):
#     print(second)
#     time.sleep(5)
# print("Happy Mew Year")

# import time
# for second in range(20,0,-1):
#     if second == 1:
#         print(str(second), "second left ")
#     else:
#         print(str(second), "seconds left")
#     time.sleep(1)
# print("Happy New Month")



import time
number = int(input("Please enter where you want to start counting from!!"))
message = str(input("Do you want Happy New Month // or Happy New Year!!"))
for second in range(number,0,-1):
    if second == 1:
        print(str(second), "second left ")
    else:
        print(str(second), "seconds left")
    time.sleep(1)
    print("Happy New Month")
    
