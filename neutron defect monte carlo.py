import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_atoms = 10000              # Number of atoms in the crystalline
num_neutrons = 1000            # Number of high-energy neutrons
neutron_energy = 5.0           # Energy of neutrons (MeV)
defect_threshold = 1.0         # Minimum energy required to cause a defect 
defect_reduction_rate = 0.002  # Fractional structural integrity loss per defect

# Each atom is represented as 1. Defects will set atoms to 0
crystal = np.ones(num_atoms)

# Defect probability based on neutron energy
def defect_probability(neutron_energy, threshold):
    if neutron_energy >= threshold:
        return min(1.0, neutron_energy / 10.0)  # Higher energy, higher chance
    return 0.0

# Simulate neutron interactions
for i in range(num_neutrons):
    # Randomly select an atom to be hit
    hit_atom = np.random.randint(0, num_atoms)

    # Calculate the probability of causing a defect
    prob = defect_probability(neutron_energy, defect_threshold)

    # Determine if a defect occurs
    if np.random.random() < prob:
        crystal[hit_atom] = 0  # Defect occurs

# Result calculation
num_defects = np.sum(crystal == 0)
structural_integrity = max(0.0, 1.0 - num_defects * defect_reduction_rate)


print(f"Total atoms: {num_atoms}")
print(f"Number of neutrons: {num_neutrons}")
print(f"Number of defects: {num_defects}")
print(f"Structural integrity: {structural_integrity * 100:.2f}%")

plt.figure(figsize=(10, 6))
plt.bar(["Intact", "Defective"], [num_atoms - num_defects, num_defects], color=["green", "red"])
plt.title("Crystal Integrity After Neutron Irradiation")
plt.ylabel("Number of Atoms")
plt.show()