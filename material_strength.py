# (c) 2025 Lara Yzabelle A. Barrera, Rissa A. Niepes
# An Engineering Calculations using functions.

def material_strength_calculation_for_steel():
    F = float(input("Enter the force applied to the beam (N): "))
    A = float(input("Enter the cross-sectional area of the beam (mm**2): "))
    sigma = F / A
    
    print(f"So, the stress on the beam is {sigma:.2f} Pa.")
if __name__ == "__main__":
    material_strength_calculation_for_steel()