import math

def menu():
    print("\n--- CALCULATEUR AÉRODYNAMIQUE ---")
    print("1. Calculer la Portance et la Traînée (Aérofoil)")
    print("2. Calculer la Poussée et le Couple (Hélice)")
    print("3. Calculer le Nombre de Reynolds")
    print("4. Méthode des Éléments de Pale (BEM) Simplifiée")
    print("5. Quitter")
    choice = input("Choisissez une option (1-5): ")
    return choice

def lift_drag():
    rho = float(input("Densité de l'air (kg/m³): "))
    V = float(input("Vitesse (m/s): "))
    S = float(input("Surface (m²): "))
    CL = float(input("Coefficient de portance (CL): "))
    CD = float(input("Coefficient de traînée (CD): "))
    
    L = 0.5 * rho * V**2 * S * CL
    D = 0.5 * rho * V**2 * S * CD
    
    print(f"\nPortance: {L:.2f} N")
    print(f"Traînée: {D:.2f} N")

def propeller_thrust_torque():
    CT = float(input("Coefficient de poussée (CT): "))
    CQ = float(input("Coefficient de couple (CQ): "))
    D = float(input("Diamètre de l'hélice (m): "))
    rpm = float(input("Vitesse de rotation (tr/min): "))
    rho = float(input("Densité de l'air (kg/m³): "))
    
    omega = rpm * 2 * math.pi / 60  # Conversion RPM → rad/s
    T = (CT * rho * (omega**2) * (D**4)) / 8
    Q = (CQ * rho * (omega**2) * (D**5)) / 8
    
    print(f"\nPoussée: {T:.2f} N")
    print(f"Couple: {Q:.2f} Nm")

def reynolds_number():
    print("Choisissez le type de viscosité (1: dynamique, 2: cinématique):")
    choice = int(input("Entrez 1 ou 2: "))
    
    rho = float(input("Densité de l'air (kg/m³): "))
    V = float(input("Vitesse (m/s): "))
    L = float(input("Longueur caractéristique (m): "))
    
    if choice == 1:
        mu = float(input("Viscosité dynamique (Pa·s): "))
        Re = (rho * V * L) / mu
    else:
        nu = float(input("Viscosité cinématique (m²/s): "))
        Re = (V * L) / nu
    
    print(f"\nNombre de Reynolds: {Re:.2e}")

def blade_element_method():
    R = float(input("Rayon de la pale (m): "))
    omega = float(input("Vitesse de rotation (rad/s): "))
    rho = float(input("Densité de l'air (kg/m³): "))
    B = int(input("Nombre de pales: "))
    c = float(input("Corde de la pale (m): "))
    CL = float(input("Coefficient de portance (CL): "))
    CD = float(input("Coefficient de traînée (CD): "))
    V_in = float(input("Vitesse d'intrusion axiale (m/s): "))
    
    N = 10  # Nombre de segments de pale
    dr = R / N
    
    T_total = 0
    Q_total = 0
    
    for i in range(N):
        r = (i + 0.5) * dr  # Position au milieu du segment
        u = omega * r       # Vitesse tangentielle
        W = math.sqrt(u**2 + V_in**2)  # Vitesse résultante
        phi = math.atan(V_in / u)      # Angle d'inclinaison du flux
        
        sin_phi = V_in / W
        cos_phi = u / W
        
        # Contributions par unité de longueur
        L_per_unit = 0.5 * rho * (W**2) * c * CL * sin_phi
        D_per_unit = 0.5 * rho * (W**2) * c * CD * cos_phi
        
        # Contributions totales pour le segment
        dT = B * L_per_unit * dr
        dQ = B * D_per_unit * r * dr
        
        T_total += dT
        Q_total += dQ
    
    print(f"\nPoussée totale: {T_total:.2f} N")
    print(f"Couple total: {Q_total:.2f} Nm")

# Boucle principale
while True:
    choice = menu()
    
    if choice == '1':
        lift_drag()
    elif choice == '2':
        propeller_thrust_torque()
    elif choice == '3':
        reynolds_number()
    elif choice == '4':
        blade_element_method()
    elif choice == '5':
        print("Au revoir!")
        break
    else:
        print("Option invalide. Réessayez.")
