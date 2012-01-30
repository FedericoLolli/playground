import fox
import time

# Define myled as the led labeled "L1" on the 
# Daisy11 module wired on D2 connector

Out1 = fox.Daisy19('D2','first','O1')
Out2 = fox.Daisy19('D2','first','O2')
Out3 = fox.Daisy19('D2','first','O3')
Out4 = fox.Daisy19('D2','first','O4')
 
while True:
	Out1.on()
	Out2.on()
	Out3.on()
	Out4.on()
	time.sleep(0.2)
	Out1.off()
	Out2.off()
	Out3.off()
	Out4.off()
	time.sleep(0.2)
