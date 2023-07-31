#For the numbers in the range of 1 to 100
#Write a function to print "fizz" if the number is divisible by 3,
# print "Buzz"  if the number is divisble by 5 and print "FizzBuzz if the number is both divisible by 3 and 5"

# def fizz_buzz():
#     for number in range(20, 61):
#         if number % 3  ==0 and number % 5 ==0:
#             print(str(number)+ ":FizzBuzz")
#         elif number % 3 and 1 == 0:
#             print(str(number)+":Fizz")
#         elif number % 5 and 1 ==0:
#             print(str(number)+":Buzz")



# fizz_buzz()












def checkPrime(num):   
    if num < 2:
        return 0
    else:
        x = num // 2
        for j in range(2, x + 1):
            if num % j == 0:
                return 0
    return 1
a, b = 20,60
for i in range(a, b + 1):
    if checkPrime(i):
            print(i, "Is a prime number")#
            continue
            print(i, end="  ")







