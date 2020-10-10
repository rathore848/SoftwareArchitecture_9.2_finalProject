import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
cardWrite = SimpleMFRC522()
try:
        text = raw_input('Enter data for writing to card')
        print ("place your tag to write: ")
        cardWrite.write(text)
        print ("Write Successfully")
finally:
        gpio.cleanup()