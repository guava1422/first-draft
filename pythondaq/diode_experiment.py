#Name: Guru Partap Khalsa
#Student number: 12581631
#Assignement: 3.6-3.7



from arduino_device import ArduinoVISADevice
import numpy as np

port = "ASRL4::INSTR"
device = ArduinoVISADevice(port=port)

#this class sets up our expriment if measuring the U-I charaterstic from a start voltage to ahn end voltage
class DiodeExperiment():
    def __init__(self):
        self.list_voltage=[]
        self.list_current=[]
        self.volt_err=[]

#this function increases the voltage sent in the arduino 
#step by step in a certain range and then saves the values in a list
    def scan(self,start,stop):
        for i in range(start,stop):
            #list which reset every value 
            U=[]
            C=[]
            #a loop rerunning each voltage a certain number of times to find the average
            for j in range(3):
                device.set_output_value(value= i)
                U.append(device.get_input_voltage(channel=1)-device.get_input_voltage(channel=2))
                C.append(device.get_input_voltage(channel=2)/220)
            #saves the average of each value and the error on it
            self.list_voltage.append(np.mean(U))
            self.volt_err.append(np.std(U))
            self.list_current.append(np.mean(C)/220)
    #function to return the list of voltages
    def voltage(self):
        return self.list_voltage
    #function to return errors on voltage
    def voltage_error(self):
        return self.volt_err
    #function to return current list
    def current(self):
        return self.list_current


