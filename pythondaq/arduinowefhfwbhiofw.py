from arduino_device import list_devices, ArduinoVISADevice

# we willen, voor de zekerheid, nog steeds een functie om
# een lijst van poorten te krijgen, _buiten_ de class
print(list_devices())
# de poort moet je mogelijk zelf aanpassen
port = "ASRL4::INSTR"
# zorg dat de device al geopend wordt in de __init__()
device = ArduinoVISADevice(port=port)
# print identification string
print(device.get_identification())
# set OUTPUT voltage on channel 0, using ADC values (0 - 1023)
device.set_output_value(value= 0)
# get the previously set OUTPUT voltage in ADC values (0 - 1023)
ch0_value = device.get_output_value()
# measure the voltage on INPUT channel 2 in ADC values (0 - 1023)
ch2_value = device.get_input_value(channel=2)
# measure the voltage on INPUT channel 2 in volts (0 - 3.3 V)
ch2_voltage = device.get_input_voltage(channel=2)

print(ch2_value,ch0_value)