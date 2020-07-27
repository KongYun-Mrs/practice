import datetime
import time

time1 = time.ctime()
print(time1)
time_seconds = time.time()  # 生成时间戳
print(time_seconds)

dateArray = datetime.datetime.fromtimestamp(time_seconds)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)


timeArray = time.localtime(time_seconds)
print(timeArray)
time_orig = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
print(time_orig)
