import numpy as np
import matplotlib.pyplot as plt

def ramp(t):
    return np.maximum(0, t)

def x(t):
    return ramp(t) - 2 * ramp(t - 1) + ramp(t + 2)

# Define the time range
t = np.linspace(-5, 5, 1000)

# Compute the values of x(t)
x_t = x(t)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='x(t) = r(t) - 2r(t-1) + r(t+2)')
plt.title('Plot of x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()
