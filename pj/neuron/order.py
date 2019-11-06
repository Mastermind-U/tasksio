import numpy as np



def generate_vectors():
    from itertools import product as p
    return(p(range(2), repeat=2))

def f(x):
    return(x[0] or x[1])

x_vectors = generate_vectors()
t_vector = np.array([f(x) for x in x_vectors])
x_vectors = generate_vectors()
nu = 0.01
weight = np.array([0., 0.])
epoch = 1
error = 1

while error != 0:
    x_vectors = generate_vectors()
    print(f'\n*************** epoch {epoch} ***************')
    print(f'weight = {weight}')
    print(f'_____________________________________________')
    error = 0
    for i, x_vec in enumerate(x_vectors):
        net = sum(x_vec[j]*weight[j] for j in range(2))
        if net >= 0.5:
            y = 1
        else:
            y = 0

        delta = t_vector[i] - y
        err = t_vector[i] - net
        print(f'| net = {net:.3f} | y = {y}| t = {t_vector[i]} | delta = {delta:.3f} |')
        if delta != 0:
            error += 1
        weight = [weight[j] + nu * delta * x_vec[j] for j in range(2)]
    epoch += 1
    print(f'¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print(f'{error} errors\n')