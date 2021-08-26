import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.2)
y = np.sin(x)
z = np.cos(x)

print(z)

plt.plot(x, y)