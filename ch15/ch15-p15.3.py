import matplotlib.pyplot as plt
import numpy as np


G = M = 1


def robot_fn(r):
    C = (4 * G * M) / 3
    return ((-2/3) * (r**(3/2)) / np.sqrt(2 * G * M)) + C


def photon_fn(r):
    term_1 = -r
    term_2 = np.sqrt(8 * G * M * r)
    term_3 = -(4 * G * M) * np.log(1 + np.sqrt(r / (2 * G * M)))
    C = 2 - 4 + (4 * np.log(2))
    return term_1 + term_2 + term_3 + C


def main():
    r = np.linspace(0, 3, 500)
    fig, ax = plt.subplots()
    ax.plot(r, robot_fn(r), label="robot")
    ax.plot(r, photon_fn(r), label="photon")
    ax.set_xlabel("r")
    ax.set_ylabel("tº")
    ax.grid(True)
    ax.set_title("Wordlines assuming GM = 1", va='bottom')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
