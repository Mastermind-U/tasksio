import matplotlib.pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = sorted(variance, reverse=True)
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label='Dispersion')
plt.plot(xs, bias_squared, 'r-', label='Bias Squared')
plt.plot(xs, total_error, 'b:', label='Total Error')
plt.legend(loc=9)
plt.xlabel('Сложность модели')
plt.title('Компромисс между смещением и дисперсией')
plt.show()
