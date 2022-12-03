import RPi.GPIO as GPIO
import time,signal,sys
GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24
GPIO.setup(2,GPIO.OUT)
def close(signal,frame):
  print("\n Turning Of Ultra-Sonic")
  GPIO.cleanup()
  sys.exit(0)W
  signal.signal(signal.SIGINT,close)
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)
while True :
   GPIO.output(TRIG,True)
   time.sleep(0.00001)
   GPIO.output(TRIG,False)
   startTime = time.time()
   stopTime = time.time()
   while 0 == GPIO.input(ECHO):
     startTime = time.time()
   while 1 == GPIO.input(ECHO):

    stopTime = time.time()
   TimeElapsed = stopTime - startTime
   distance = (TimeElapsed * 34300)/2

   print("Distance :%.1f cm"%distance)
   time.sleep(1)

   if distance < 10:
     GPIO.output(2,GPIO.HIGH)
     print("Garbage is 75% or Above .")
   elif distance < 20:
     GPIO.output(2,GPIO.HIGH)
     print("Garbage is 50% or Above .")
   else:
     GPIO.output(2,GPIO.LOW)+
     print(" Dust- Bin is Empty or Not Much More Garbage.")
