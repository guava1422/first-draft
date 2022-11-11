#Name: Guru Partap Khalsa
#Student number: 12581631
#Assignement: 3.6-3.7


from diode_experiment import DiodeExperiment
import matplotlib.pyplot as plt

#plot of experiment
diode = DiodeExperiment()
diode.scan(start=0,stop=1024)
fig= plt.figure()
plt.scatter(diode.voltage(),diode.current())
plt.errorbar(diode.voltage(),diode.current(),xerr=diode.voltage_error(), fmt="o")
plt.xlabel('voltage')
plt.ylabel('current')
plt.show() 
