import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    t = np.arange(-1, 2, .01)
    s = np.sin(2 * np.pi * t)

    plt.plot(t, s)
    plt.show()
    print(1)
