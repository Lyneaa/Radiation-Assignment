import numpy as np
import matplotlib.pyplot as plt

thermal_conductivity = 2.5  # W/m·K
specific_heat_capacity = 900  # J/kg·K
density = 2500  # kg/m^3
energy_deposition_rate = 5e6  # W/m^3
irradiation_duration = 24 * 3600  # seconds 
initial_temperature = 300  # K
cube_length = 0.5  # m

volume = cube_length**3  # m^3
mass = density * volume  # kg

# Energy deposited in the material
energy_deposited = energy_deposition_rate * volume * irradiation_duration  # J

# Temperature rise 
temperature_rise = energy_deposited / (mass * specific_heat_capacity)
final_temperature = initial_temperature + temperature_rise

# Temperature over time
time_steps = np.linspace(0, irradiation_duration, 500)  # Time steps
temperature_over_time = initial_temperature + (energy_deposition_rate * volume * time_steps) / (mass * specific_heat_capacity)

# Estimation for certain values
# Assuming structural integrity decreases linearly with temperature above a threshold (e.g., 600 K)
threshold_temperature = 600  # K 
integrity_decrease_rate = 0.01  # rate of decrease per K above threshold
structural_integrity = np.maximum(100 - integrity_decrease_rate * np.maximum(temperature_over_time - threshold_temperature, 0), 0)

# Find the time when the temperature reaches 600 K
time_to_threshold_index = np.where(temperature_over_time >= threshold_temperature)[0][0]
time_to_threshold = time_steps[time_to_threshold_index]  # Time in s
time_to_threshold_hours = time_to_threshold / 3600 # Convert to hours

print(f"The temperature reaches {threshold_temperature} K at approximately {time_to_threshold_hours:.4f} hours.")
print(f"Initial Temperature: {initial_temperature} K")
print(f"Final Temperature after 24 hours: {final_temperature:.2f} K")
print(f"Temperature Rise: {temperature_rise:.2f} K")

# Find the time when structural integrity reaches 0
time_to_failure_index = np.where(structural_integrity == 0)[0][0]
time_to_failure = time_steps[time_to_failure_index]  # Time in seconds
time_to_failure_hours = time_to_failure / 3600 # Convert to hours
print(f"The structural integrity reaches 0 at approximately {time_to_failure_hours:.2f} hours.")

plt.figure(figsize=(10, 6))
plt.plot(time_steps / 3600, temperature_over_time, label="Temperature (K)", color="blue")
plt.axhline(y=threshold_temperature, color="red", linestyle="--", label="Threshold Temperature")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (K)")
plt.title("Temperature Increase Over Time Due to Neutron Radiation")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(time_steps / 3600, structural_integrity, label="Structural Integrity (%)", color="green")
plt.xlabel("Time (hours)")
plt.ylabel("Structural Integrity (%)")
plt.title("Structural Integrity Over Time")
plt.grid()
plt.legend()
plt.show()
