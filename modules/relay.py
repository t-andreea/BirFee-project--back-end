import RPi.GPIO as GPIO

class Relay(object):
   __instance = None  #the Relay object
   
   @staticmethod
   def get_instance(pin):
      if Relay.__instance is None:
         Relay.__instance = Relay.__Relay(pin)
      return Relay.__instance

   class __Relay(object):
      __status = False
	
      def __init__(self, pin_number):
         self.__pin = pin_number
         GPIO.setmode(GPIO.BOARD)
         GPIO.setup(self.__pin, GPIO.OUT)
	
      def on(self):
         GPIO.output(self.__pin, GPIO.HIGH)
         self.__status = True
	
      def off(self):
         GPIO.output(self.__pin, GPIO.LOW)
         self.__status = False
	
      def status(self):
         return self.__status
