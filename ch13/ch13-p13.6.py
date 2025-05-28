import matplotlib.pyplot as plt
import numpy as np


def I_fn(u0, t_te):
    q = np.sqrt(1 + (4/((t_te**2) + (u0**2))))
    return 0.5 * ((1/q) + q)


def main():
    fig, ax = plt.subplots()
    t_te = np.arange(-2.5, 2.5, 0.01)
    ax.grid(True)
    ax.set_title("")
    for u0 in [0.06, 0.1, 0.3, 0.8, 1]:
        I = I_fn(u0, t_te)
        ax.plot(t_te, I, label=f"u_0={u0}")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
