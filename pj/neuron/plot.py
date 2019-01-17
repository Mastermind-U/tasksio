import matplotlib.pyplot as plt

def plot(x, y):
	fig, ax = plt.subplots(figsize=(4, 4))
	ax.stackplot(x, y, labels=['Dynamics'], colors=['c'])

	ax.scatter(x=x, y=y, marker='s', c='g')
	ax.set_title('Education process')
	ax.set_xlabel('$Epochs$')
	ax.set_ylabel('$Err$')
	ax.legend(loc='upper left')
	fig.tight_layout()

	plt.show()
