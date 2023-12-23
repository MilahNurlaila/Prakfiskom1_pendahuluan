class ChargedParticle:
    def __init__(self, charge, mass):
        self.charge = charge
        self.mass = mass
        self.position = 0
        self.velocity = 0

    def apply_force(self, force, time_step):
        acceleration = force / self.mass
        self.velocity += acceleration * time_step
        self.position += self.velocity * time_step

def calculate_force(q1, q2, r):
    k = 8.9875 * (10**9)  # Coulomb's constant
    return k * abs(q1 * q2) / (r**2)

def simulate_interaction(particle1, particle2, distance, time_step, duration):
    for _ in range(int(duration / time_step)):
        force = calculate_force(particle1.charge, particle2.charge, distance)
        particle1.apply_force(force, time_step)
        particle2.apply_force(-force, time_step)
        print(f"Particle 1 Position: {particle1.position:.2f}, Particle 2 Position: {particle2.position:.2f}")

# Example usage:
particle1 = ChargedParticle(1.6 * (10**-19), 9.1 * (10**-31))  # Charge and mass of an electron
particle2 = ChargedParticle(-1.6 * (10**-19), 9.1 * (10**-31))  # Charge and mass of an electron
initial_distance = 1e-10  # Initial distance between particles (e.g., 1 angstrom)
time_step = 1e-17  # Time step for simulation (e.g., 10 femtoseconds)
simulation_duration = 1e-14  # Duration of simulation (e.g., 1 picosecond)

simulate_interaction(particle1, particle2, initial_distance, time_step, simulation_duration)
