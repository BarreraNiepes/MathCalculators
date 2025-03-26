# (c) 2025 Lara Yzabelle A. Barrera, Rissa A. Niepes
# An Engineering Calculations using functions.

def concrete_volume_calculation():
    L = float(input("Enter the length of the sidewalk (m): "))
    W = float(input("Enter the width of the sidewalk (m): "))
    D = float(input("Enter the depth of the sidewalk (m): "))
    V = L * W * D
    
    print(f"So, you need {V:.2f} cubic meters of concrete.")
if __name__ == "__main__":
    concrete_volume_calculation()