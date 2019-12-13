import matplotlib.pyplot as plt
import numpy as np

years = [y for y in range(1950, 2011, 10)]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 15958.3]
plt.plot(years, gdp, color='green', marker='o')
plt.title('Nominal GDP')
plt.ylabel('Billion $')
plt.grid(color='r', linestyle='-', linewidth=2)
plt.show()
