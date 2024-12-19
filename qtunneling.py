import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
me = 9.10938356e-31   # e mass (kg)
e = 1.602176634e-19   # Elementary charge (C)

# Func Tunneling probability
def tunneling_probability(U, E, m, a):
    """
    Calculate tunneling probability for a particle.
    U: Potential barrier height (J)
    E: Particle energy (J)
    m: Particle mass (kg)
    a: Barrier width (m)
    """
    if E >= U:
        return 1  # No tunneling if the particle energy >= the barrier height
    kappa = np.sqrt(2 * m * (U - E)) / hbar
    return np.exp(-2 * kappa * a)

# Parameters
E = 5 * e      # Particle energy (5 eV convert to J)
m = me         # Mass of e
a = 1e-10      # Barrier width (1 Angstrom)

# Range of potential barrier heights (U) in eV
U_range_eV = np.linspace(5, 20, 200)  # Barrier height
U_range_J = U_range_eV * e # Convert to J

tunneling_probs = [tunneling_probability(U, E, m, a) for U in U_range_J]

plt.figure(figsize=(8, 6))
plt.plot(U_range_eV, tunneling_probs, label=f"Particle Energy = {E/e:.2f} eV", color="blue")
plt.xlabel("Barrier Height (U) [eV]")
plt.ylabel("Tunneling Probability (T)")
plt.title("Effect of Barrier Height on Tunneling Probability")
plt.grid()
plt.legend()
plt.show()
