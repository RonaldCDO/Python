import time
import numpy as np


# hours: minutes: seconds
def time_spent(classroom_time, speed_rate):

    start = time.time()
    end_time = start + classroom_time / speed_rate
    print(end_time.strftime('%H:%M:%S'))


test = [1, ':', 12, ':', 12]

print(test)
hello = '1:10:10'
# transform = test[4] + test[2]*60 + test[0]*3600
transform = [i for i in hello]
print(transform)
