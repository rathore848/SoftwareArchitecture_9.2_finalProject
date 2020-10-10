import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
CardReader = SimpleMFRC522()
print ('Scanning for a  card..')
print ('to cancel press ctrl+c')
try:
        id, text = CardReader.read()
        print (id)
        print(text)
finally:
        gpio.cleanup()