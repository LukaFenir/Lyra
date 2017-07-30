import pyttsx #text-to-speech library
import serial #serial communication library

print "que?"
while True:
    ser = serial.Serial('COM2',9600)    #opens COM port 8 with baud rate of 9600
    print "que2?"
    raw_data = ser.read(7)              #read first 7 characters from port
    msg = str(raw_data[3:6])            #extracts 3rd to 6th characters from array
                                            #cos 0-2 are junk characters in BitVoicer
        
    print msg
    ser.close()     #close serial port
        
    if(msg == 'who'):
        engine = pyttsx.init()
        engine.say('Hi there. My name is Lyra, waddup?')
        engine.runAndWait()
    if(msg == 'lik'):
        engine = pyttsx.init()
        engine.say('Yes! Who doesn\'t, are you nuts?')
        engine.runAndWait()        
    