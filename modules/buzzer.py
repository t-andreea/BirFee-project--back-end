import RPi.GPIO as GPIO
import time

class Buzzer:

    def __init__(self, pin):
        self.BuzzerPin = pin
        
        CL = [0, 131, 147, 165, 175, 196, 211, 248] # Low C Note Frequency 
        CM = [0, 262, 294, 330, 350, 393, 441, 495] # Middle C Note Frequency
        CH = [0, 525, 589, 661, 700, 786, 882, 990] # High C Note Frequency 
         
        self.song_1 = [ CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Sound Notes 1
        CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
        CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
        CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5] ]
         
        self.beat_1 = [ 1, 1, 3, 1, 1, 3, 1, 1, # Beats of song 1, 1 means 1/8 beats
        1, 1, 1, 1, 1, 1, 3, 1,
        1, 3, 1, 1, 1, 1, 1, 1,
        1, 2, 1, 1, 1, 1, 1, 1,
        1, 1, 3 ]
         
        self.song_2 = [ CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Sound Notes 2
        CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
        CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
        CM[3], CM[2], CL[5], CL[7], CM[2], CM[1] ]
         
        self.beat_2 = [ 1, 1, 2, 2, 1, 1, 2, 2, # Beats of song 2, 1 means 1/8 beats
        1, 1, 2, 2, 1, 1, 3, 1,
        1, 2, 2, 1, 1, 2, 2, 1,
        1, 2, 2, 1, 1, 3 ]

        self.setup()


    def setup(self):
	GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
	GPIO.setup(self.BuzzerPin, GPIO.OUT) # Set pins' mode is output
	
	self.Buzz = GPIO.PWM(self.BuzzerPin, 440) # 440 is initial frequency.
	self.Buzz.start(50) # Start BuzzerPin pin with 50% duty ration


    def play_song(self, song, beat):
	for i in range(1, len(song)): # Play song 1
	    self.Buzz.ChangeFrequency(song[i]) # Change the frequency along the song note
	    time.sleep(beat[i] * 0.5) # delay a note for beat * 0.5s


    def play(self):
	# while True:
	print '\n Playing song 1...'
	self.play_song(self.song_1, self.beat_1)
	time.sleep(1) # Wait a second for next song.
	 
	print '\n\n Playing song 2...'
	self.play_song(self.song_2, self.beat_2)


    def destory(self):
	self.Buzz.stop() # Stop the BuzzerPin
	GPIO.output(self.BuzzerPin, 1) # Set BuzzerPin pin to High
	GPIO.cleanup() # Release resource   




    
    
        
