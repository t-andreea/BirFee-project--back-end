import RPi.GPIO as GPIO

class Relay(object):
   __instance = dict()  #the Relay object
   
   @staticmethod
   def get_instance(pin):
      if pin in Relay.__instance:
         return Relay.__instance[pin]
      Relay.__instance[pin] = Relay.__Relay(pin)
      return Relay.__instance[pin]

   class __Relay(object):
      __status = False
	
      def __init__(self, pin_number):
         self.__pin = pin_number
         GPIO.setmode(GPIO.BOARD)
         GPIO.setup(self.__pin, GPIO.OUT)
	
      def off(self):
         GPIO.output(self.__pin, GPIO.HIGH)
         self.__status = False
	
      def on(self):
         GPIO.output(self.__pin, GPIO.LOW)
         self.__status = True
	
      def status(self):
         return self.__status
