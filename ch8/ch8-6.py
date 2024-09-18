import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    plt.figure()
    ax = plt.axes()
    t_a = np.arange(0, 8, 0.1)
    x_a = np.log((t_a/2)**2 + 1)
    plot(ax, x_a, t_a, "x/a")
    # plt.show()
    plt.savefig("ch8-6.png")

def plot(ax, x, y, label):
    ax.plot(x, y, label=label)
    ax.grid(visible=True)
    ax.legend()
    ax.set_xlabel("x/a")
    ax.set_ylabel("t/a")


if __name__ == "__main__":
    main()