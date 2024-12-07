import math
import datetime
import jdatetime
import time

print(datetime.datetime.today())

while True:
    time.sleep(1)
    mainTime = datetime.datetime.today()
    print((len((datetime.datetime.today().strftime('hh-mm-ss'))) * '\b') + mainTime)


# def DtoR(degrees):
#     radians = degrees*(math.pi/180)
#     return radians


# x = math.sin(DtoR(30))
# print(x)