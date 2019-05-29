import Adafruit_DHT

# Class responsible to get the humity and temperature from the sensor
class TempHumSensor:
	def __init__(self, pin):
		self.sign_pin = pin
		self.humidity = None
		self.temperature = None

	def getValue(self):
		# Set sensor type : Options are DHT11, DHT22 or AM2302
		sensor = Adafruit_DHT.DHT11

		# Set GPIO sensor is connected to
		gpio = self.sign_pin

		#Use read_retry method. This will retry up to 15 times to get ready a sensor reading (waiting 2 seconds between each retry)
		self.humidity, self.temperature = Adafruit_DHT.read_retry(sensor, gpio)

		#Reading the DHT11 is very sensitive to timings ans occasionally the Pi might fail to get a valid reading. So check if readings are valid
		if self.humidity is not None and self.temperature is not None:
			return "Temp={0:0.1f}*C Humidity={1:0.1f}%".format(self.temperature,self.humidity)
		else:
			return "Failed to get reading. Try again!"
