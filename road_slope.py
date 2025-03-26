# (c) 2025 Lara Yzabelle A. Barrera, Rissa A. Niepes
# An Engineering Calculations using functions.

def slope_of_a_road():
    rise = float(input("Enter the rise of the road (m): "))
    run = float(input("Enter the horizontal distance (run) (m): "))
    
    slope = (rise/run) * 100 
    
    print(f"So, the slope of the road is {slope:.2f} %")
if __name__ == "__main__":
    slope_of_a_road()