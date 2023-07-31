import time

time_object = time.localtime()
local_time = time.strftime("%m, %Y", time_object)
formatted_local_time = local_time.split(",")
local_year = int(formatted_local_time[1])

def age_generator():
    birth_year = int(input("Please enter your birth year: "))
    age = local_year - birth_year
    print(f"You are {age} years old")

age_generator()