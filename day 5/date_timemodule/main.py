import time 

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_string)


print(time.ctime(0))
print(time.ctime(1000000))
time_object = time.localtime()
print(time_object)