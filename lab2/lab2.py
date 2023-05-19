import numpy as np
import matplotlib.pyplot as plt 
from helpers import get_general_membership_function

t = 0
t_max = 50
dt = 0.1
dmu = 1

phi = -40 * np.pi /180
omega = 0 * np.pi /180
phi_min = -np.pi
phi_max = np.pi
omega_min = -np.pi/9
omega_max = np.pi/9
mu_min = -np.pi/36
mu_max = np.pi/36

phi_t, omega_t, mu_t, t_n = [], [], [], []
afile = open("results.csv", "w")
afile.write("t,phi,omega,mu\n")

while t < t_max - 0.5 * dt:
    phi_ = 200 * (phi - phi_min) / (phi_max - phi_min) - 100
    omega_ = 200 * (omega - omega_min) / (omega_max - omega_min) - 100

    mu_ = -100
    s1 = 0
    s2 = 0

    while mu_ < 100 - 0.5 * dmu:
        xi_dash = get_general_membership_function(phi_, omega_, mu_)
        s1 = s1 + mu_ * xi_dash * dmu
        s2 = s2 + xi_dash * dmu
        mu_ = mu_ + dmu

    mu_dash = s1 / s2
    mu = (mu_dash + 100) * (mu_max - mu_min) / 200 + mu_min

    phi = phi + omega * dt
    omega = omega + mu * dt

    phi_t.append(phi)
    omega_t.append(omega)
    mu_t.append(mu)
    t_n.append(t)

    afile.write(f'{t},{phi},{omega},{mu}\n')

    t = t + dt

plt.plot(t_n, phi_t, 'r')
plt.plot(t_n, omega_t, 'b')
plt.plot(t_n, mu_t, 'k')
plt.legend([r'$\phi$ - кут орієнтації', r'$\omega$ - кутова швидкість', r'$\mu$ - приведений керуючий момент'])
plt.grid(True)
plt.ylabel(r'F')
plt.xlabel('Час, с')
plt.show()

asdf = 2