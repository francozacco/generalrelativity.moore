
import matplotlib.pyplot as plt
import numpy as np


def main():
    t_t0 = np.linspace(0, 1, 500)
    fig, ax = plt.subplots()
    ax.plot(t_t0, np.cbrt(1 - t_t0))
    ax.set_xlabel("t/t0")
    ax.set_ylabel("M/M0")
    ax.grid(True)
    ax.set_title("M/M0 as a function of t/t0", va='bottom')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
