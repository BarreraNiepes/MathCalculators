# (c) 2025 Lara Yzabelle A. Barrera, Rissa A. Niepes
# An Engineering Calculations using functions.

def cement_slurry_dilution():
    V2 = float(input("Enter the final volume of slurry needed (L): "))
    C1 = float(input("Enter the initial concentration (g/L): "))
    C2 = float(input("Enter the desired concentration (g/L): "))
    V1= (V2 * C2) / C1
    
    print(f"So, you need {V1:.2f} liters of the original slurry.")
if __name__ == "__main__":
    cement_slurry_dilution()
    
