import random
from collections import Counter
from matplotlib import pyplot as plt

num_friends = [random.randint(0, 1000) for _ in range(10000)]

# %%
friend_counts = Counter(num_friends)
xs = range(1001)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 1001, 0, 25])
plt.title("Гистограмма количества друзей")
plt.xlabel("Количество друзей")
plt.ylabel("Количество людей")
plt.grid(color='w', linestyle='-.', linewidth=0.5)

plt.show()

# %%
num_points = len(num_friends)
print(num_points)
# %%
largest_value = max(num_friends)
print(largest_value)

# %%
smallest_value = min(num_friends)
print(smallest_value)

# %%
sorted_values = sorted(num_friends)
print(sorted_values[0])  # minimum
print(sorted_values[1])  # next minimum
print(sorted_values[-2])  # nex maximum


# %%
