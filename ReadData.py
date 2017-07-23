import pandas as pd
import numpy as np

x = np.arange(0, 5, 1)
y = np.array([[0.37,0.14,0.75,0.70,0.56],[0.02,0.37,0.78,0.12,
			0.17],[0.62,0.72,0.15,0.33,0.20],[0.39,0.37,0.01,
			0.12,0.53]])
			
print 			

plt.figure(figsize=(8,4))
for i in range(4):
	plt.plot(x, y[i,:], label="Temperature of Antenna ID %d" %i, color="red", linewidth=2)
	#plt.plot(x,z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)")
plt.ylabel("Degree C")

plt.title("Temperature Data of Antenna")
plt.ylim(0, 1)
#plt.xlim(0,100)

plt.legend()

plt.show()