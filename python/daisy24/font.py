import fox
import time

lcd = fox.Daisy24(0)

while True:
	lcd.clear()
	lcd.setdoublefont()
	lcd.putstring("Hello World !")

	time.sleep(1)

	lcd.clear()
	lcd.setsinglefont()
	lcd.putstring("Hello World !")

	time.sleep(1)

