import math 
import matplotlib.pyplot as plt

EPSILON = 10e-12


def r_fn(GM, l, dtau, r_n, r_nm1):
    l_2 = l**2
    right_side = (dtau**2) * (-(GM/(r_n**2)) + (l_2/(r_n**3)) - ((3 * GM * l_2)/(r_n**4)))
    ans = right_side + (2 * r_n) - r_nm1
    if ans < 0:
        return EPSILON
    return ans


def phi_fn(l, dtau, r_n, r_np1, phi_n):
    return ((4 * l * dtau)/((r_np1 + r_n)**2)) + phi_n


def main():
    steps = 5000
    GM = 1

    r_init = 50 * GM
    _l_circ = r_init / (math.sqrt((r_init/GM) - 3))
    _dphidtau_circ = _l_circ / (r_init**2)
    _tau = 2 * math.pi * ((r_init**2) / _l_circ)
    dtau = _tau / 500  # For spiraling orbits set dtau = 0.2
    dphidtau_init = 0.75 * _dphidtau_circ  # Spiraling orbits starts at 0.52 
    phi_init = 0.5 * dphidtau_init * dtau
    l = (r_init**2) * (dphidtau_init)

    r_list = [r_init, r_init]
    phi_list = [0, phi_init]
    for i in range(1, steps):
        r_list.append(
            r_fn(GM, l, dtau, r_list[i], r_list[i - 1])
        )
        phi_list.append(
            phi_fn(l, dtau, r_list[i], r_list[i + 1], phi_list[i])
        )
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(phi_list, r_list)
    ax.set_rticks([r_init])
    ax.set_rlabel_position(0)
    ax.grid(True)
    ax.set_title("Precession of the perihelion", va='bottom')
    plt.show()

if __name__ == "__main__":
    main()
