# (c) 2025 Lara Yzabelle A. Barrera, Rissa A. Niepes
# An Engineering Calculations using functions.

def load_distribution_on_a_beam():
    w = float(input("Enter the uniform load (N/m): "))
    L = float(input("Enter the length of the beam (m): "))
    
    F = w * L 
    
    print(f"So, the total load acting on the beam is {F:.2f} N")
if __name__ == "__main__":
    load_distribution_on_a_beam()