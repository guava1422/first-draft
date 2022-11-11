from arduino_device import ArduinoVISADevice


port = "ASRL4::INSTR"
device = ArduinoVISADevice(port=port)


class DiodeExperiment():
    def __init__(self):
        self.list_voltage=[]
        self.list_current=[]
    def scan(self):
        for i in range(700,1024):
            device.set_output_value(value= i)
            V_ch1 = int(device.get_input_value(channel=1))*(3.3/1023)
            V_ch2 = int(device.get_input_value(channel=2))*(3.3/1023)
            self.list_voltage.append(V_ch1-V_ch2)
            self.list_current.append(V_ch2/220)

    def voltage(self):
        return self.list_voltage
    
    def current(self):
        return self.list_current
