from sense_hat import SenseHat
sense = SenseHat()

sense.clear()


print "Pressure: %d [millibar]" % (sense.get_pressure())

print "\nHumidity: %d [%%]" % (sense.get_humidity())

print "\nTemp(humidity): %d [Celsius]" % sense.get_temperature_from_humidity()
print "Temp(pressure): %d" % sense.get_temperature_from_pressure()
print "Temp: %d" % sense.get_temperature()
