#Name: Guru Partap Khalsa
#Student number: 12581631
#Assignement: 3.4-3.5





import pyvisa
rm = pyvisa.ResourceManager("@py")

#this shows all devices
def list_devices():
    return rm.list_resources()


#This class sets up commands from the arduino to further code
class ArduinoVISADevice():
    def __init__(self,port):
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")
# Gives the identity of the device plugged in
    def get_identification(self):
        return self.device.query("*IDN?")

#sets the voltage the arduino will send to the LED
    def set_output_value(self,value):
        self.value=value
        return self.device.query(f"OUT:CH0 {value}")

#Shows the output voltage value we chose
    def get_output_value(self):
        return self.value

#shows the measured value of the voltage across a specific channel
    def get_input_value(self,channel):
        return self.device.query(f"MEAS:CH{channel}?")
#converts the number of the output value to a real voltage value
    def get_input_voltage(self,channel):
        return (3.3/1023)*int(self.device.query(f"MEAS:CH{channel}?"))



