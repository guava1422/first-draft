from diode_experiment import DiodeExperiment
import matplotlib.pyplot as plt

diode = DiodeExperiment()

diode.scan()
fig= plt.figure()
plt.scatter(diode.voltage(),diode.current())
plt.show()  