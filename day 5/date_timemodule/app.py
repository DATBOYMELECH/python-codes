import time




time_object = time.localtime()

local_time = time.strftime("%B %D, %Y ,%H, %M, %S", time_object)
print(local_time)