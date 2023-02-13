import time
import math
from Motor import *
from Ultrasonic import *


# The left side motor have more power
# under this situation it go stright line 
# change by the k value and distance to the taget form wall
def forward(k,target,current):
    weight = k*(current-target)
    temp1 = int(weight /2)
    temp2 = int(weight )
    print("k:"+str(k))
    print("distance:"+str(target))
    print("current:"+str(current))
    print("weight:"+str(weight))
    print("speed:"+str(temp1)+str(temp1))
    print("------------------------------")
    PWM.setMotorModel(temp1,temp1,temp2,temp2)

# ultrasonic to get distance
ultrasonic=Ultrasonic()

# set the distance to inf at start
distance = math.inf

# while loop will stop until in the range 45 to 50
# get distance from ultrasonic
while(distance > 50 or distance < 45):
    distance = ultrasonic.get_distance()
    print ("Distance is "+str(distance)+"CM")
    forward(200,50,distance)
    time.sleep(0.05)


# turn off motor
PWM.setMotorModel(0,0,0,0)



# k at 200
# 100cm 0.69s 0.75s 0.68s 0.73s 0.71s
# 90cm 0.71s 1.01s 0.84s 0.81s 0.78s
# 80cm 0.70s 0.64s 0.98s 0.90s 0.73s
# 70cm 0.81s 0.77s 0.79s 0.81s 0.72s
# 60cm 0.92s 1.19s 0.96s 1.03s 0.93s

# at 100cm
# k = 200: 0.69s 0.75s 0.68s 0.73s 0.71s
# distance 42 to 48 
# k = 100: 1.01s 0.99s 0.84s 1.03s 0.86s
# distance 45 to 50
# k = 50: 1.03s 1.21s 1.25s 1.29s 1.23s 
# distance 48 to 50