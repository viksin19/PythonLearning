import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
plt.plot(x, y, label='Sin')
y1 = np.cos(x)

plt.plot(x, y1, label='Cos')

plt.xlabel('x-label')
plt.ylabel('y-label')
plt.title('Sin-Cos function')

plt.show()
