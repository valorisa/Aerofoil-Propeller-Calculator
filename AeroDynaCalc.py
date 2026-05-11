"""
AeroDynaCalc - Calculateur aérodynamique pour profils d'aile et hélices

Outil pédagogique et de prototypage rapide développé dans le cadre de travaux de recherche en aéronautique.
Implémente les méthodes analytiques classiques (BEMT, équations de portance/traînée) pour prédire
les performances aérodynamiques.

Auteur: valorisa
Licence: MIT
GitHub: https://github.com/valorisa/Aerofoil-Propeller-Calculator
"""

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
    """
    Calcule la portance (Lift) et la traînée (Drag) d'un profil d'aile.
    Utilise les équations aérodynamiques classiques avec la pression dynamique (q = 0.5*ρ*V²).
    """
    try:
        rho = float(input("Densité de l'air (kg/m³): "))
        if rho <= 0:
            raise ValueError("La densité doit être strictement positive")
        if rho < 0.5 or rho > 2.0:
            print("⚠️  WARNING: Densité inhabituelle. À 15°C au niveau de la mer: ρ ≈ 1.225 kg/m³")

        V = float(input("Vitesse (m/s): "))
        if V < 0:
            raise ValueError("La vitesse ne peut pas être négative")
        if V > 100:
            print("⚠️  WARNING: Vitesse élevée. Effets de compressibilité possibles (Mach > 0.3)")

        S = float(input("Surface (m²): "))
        if S <= 0:
            raise ValueError("La surface doit être strictement positive")

        CL = float(input("Coefficient de portance (CL): "))
        if not -0.5 <= CL <= 2.5:
            print("⚠️  WARNING: CL inhabituel. Plage typique: 0 à 1.5 (max théorique ~2.0)")

        CD = float(input("Coefficient de traînée (CD): "))
        if CD < 0:
            raise ValueError("Le coefficient de traînée ne peut pas être négatif")
        if CD > 0.5:
            print("⚠️  WARNING: CD élevé. Profils standards: CD < 0.1")

        # Pression dynamique : q = 0.5 * ρ * V²
        # Portance : L = q * S * CL
        L = 0.5 * rho * V**2 * S * CL
        D = 0.5 * rho * V**2 * S * CD

        print(f"\nPortance: {L:.2f} N")
        print(f"Traînée: {D:.2f} N")

    except ValueError as e:
        print(f"\n❌ ERREUR: {e}")
        print("Veuillez entrer des valeurs numériques valides.")

def propeller_thrust_torque():
    """
    Calcule la poussée (Thrust) et le couple (Torque) d'une hélice.
    Utilise les coefficients adimensionnels CT et CQ dérivés de la théorie de quantité de mouvement.
    Formules : T = CT × ρ × n² × D⁴  et  Q = CQ × ρ × n² × D⁵
    où n est la vitesse de rotation en rps (révolutions par seconde).
    """
    try:
        CT = float(input("Coefficient de poussée (CT): "))
        if not 0.001 <= CT <= 0.3:
            print("⚠️  WARNING: CT inhabituel. Plage typique hélices: 0.01 à 0.15")

        CQ = float(input("Coefficient de couple (CQ): "))
        if not 0.0001 <= CQ <= 0.1:
            print("⚠️  WARNING: CQ inhabituel. Plage typique hélices: 0.005 à 0.05")

        D = float(input("Diamètre de l'hélice (m): "))
        if D <= 0:
            raise ValueError("Le diamètre doit être strictement positif")
        if D < 0.05 or D > 2.0:
            print("⚠️  WARNING: Diamètre inhabituel. Petits UAVs: 0.15-0.50m")

        rpm = float(input("Vitesse de rotation (tr/min): "))
        if rpm <= 0:
            raise ValueError("La vitesse de rotation doit être strictement positive")
        if rpm > 15000:
            print("⚠️  WARNING: RPM très élevé. Risque vitesse bout de pale supersonique")

        rho = float(input("Densité de l'air (kg/m³): "))
        if rho <= 0:
            raise ValueError("La densité doit être strictement positive")
        if rho < 0.5 or rho > 2.0:
            print("⚠️  WARNING: Densité inhabituelle. Standard: ρ ≈ 1.225 kg/m³")

        # Conversion RPM → rps (révolutions par seconde) : n = RPM / 60
        n = rpm / 60

        # Formules standard de la théorie de quantité de mouvement
        # T = CT × ρ × n² × D⁴  (McCormick 1995, Leishman 2006)
        # Q = CQ × ρ × n² × D⁵
        T = CT * rho * (n**2) * (D**4)
        Q = CQ * rho * (n**2) * (D**5)

        print(f"\nPoussée: {T:.2f} N")
        print(f"Couple: {Q:.2f} Nm")

    except ValueError as e:
        print(f"\n❌ ERREUR: {e}")
        print("Veuillez entrer des valeurs numériques valides.")

def reynolds_number():
    """
    Calcule le nombre de Reynolds : Re = (ρ * V * L) / μ  ou  Re = (V * L) / ν
    Le nombre de Reynolds caractérise le régime d'écoulement (laminaire < 10⁵ < turbulent).
    Critique pour déterminer les coefficients aérodynamiques (CL, CD) d'un profil.
    """
    try:
        print("Choisissez le type de viscosité (1: dynamique, 2: cinématique):")
        choice = int(input("Entrez 1 ou 2: "))

        if choice not in [1, 2]:
            raise ValueError("Choix invalide. Entrez 1 ou 2.")

        rho = float(input("Densité de l'air (kg/m³): "))
        if rho <= 0:
            raise ValueError("La densité doit être strictement positive")

        V = float(input("Vitesse (m/s): "))
        if V < 0:
            raise ValueError("La vitesse ne peut pas être négative")

        L = float(input("Longueur caractéristique (m): "))
        if L <= 0:
            raise ValueError("La longueur caractéristique doit être strictement positive")

        if choice == 1:
            mu = float(input("Viscosité dynamique (Pa·s): "))
            if mu <= 0:
                raise ValueError("La viscosité dynamique doit être strictement positive")
            if mu < 1e-6 or mu > 1e-4:
                print("⚠️  WARNING: μ inhabituelle. À 15°C: μ ≈ 1.81×10⁻⁵ Pa·s")
            # Re avec viscosité dynamique : μ typique à 15°C ≈ 1.81×10⁻⁵ Pa·s
            Re = (rho * V * L) / mu
        else:
            nu = float(input("Viscosité cinématique (m²/s): "))
            if nu <= 0:
                raise ValueError("La viscosité cinématique doit être strictement positive")
            if nu < 1e-6 or nu > 1e-4:
                print("⚠️  WARNING: ν inhabituelle. À 15°C: ν ≈ 1.48×10⁻⁵ m²/s")
            # Re avec viscosité cinématique : ν = μ/ρ, typique à 15°C ≈ 1.48×10⁻⁵ m²/s
            Re = (V * L) / nu

        print(f"\nNombre de Reynolds: {Re:.2e}")

        # Interprétation du régime
        if Re < 2300:
            print("→ Régime LAMINAIRE")
        elif Re < 4000:
            print("→ Régime TRANSITOIRE")
        else:
            print("→ Régime TURBULENT")

    except ValueError as e:
        print(f"\n❌ ERREUR: {e}")
        print("Veuillez entrer des valeurs numériques valides.")

def blade_element_method():
    """
    Implémentation simplifiée de BEMT (Blade Element Momentum Theory).
    Combine la théorie de quantité de mouvement (actuator disk) avec l'analyse par éléments de pale.

    Hypothèses simplificatrices :
    - Pas de facteurs d'induction (a, a')
    - CL et CD constants sur toute la pale (pas d'interpolation Reynolds)
    - Pas de correction de perte en bout de pale (Prandtl tip-loss)

    Pour une implémentation complète, voir pyBEMT : https://github.com/ketgiljarhus/pybemt
    """
    try:
        R = float(input("Rayon de la pale (m): "))
        if R <= 0:
            raise ValueError("Le rayon doit être strictement positif")

        omega = float(input("Vitesse de rotation (rad/s): "))
        if omega <= 0:
            raise ValueError("La vitesse de rotation doit être strictement positive")

        rho = float(input("Densité de l'air (kg/m³): "))
        if rho <= 0:
            raise ValueError("La densité doit être strictement positive")

        B = int(input("Nombre de pales: "))
        if B < 2 or B > 8:
            print("⚠️  WARNING: Nombre de pales inhabituel. Hélices courantes: 2-4 pales")

        c = float(input("Corde de la pale (m): "))
        if c <= 0:
            raise ValueError("La corde doit être strictement positive")
        if c > R:
            print("⚠️  WARNING: Corde supérieure au rayon (géométrie inhabituelle)")

        CL = float(input("Coefficient de portance (CL): "))
        if not -0.5 <= CL <= 2.5:
            print("⚠️  WARNING: CL inhabituel. Plage typique: 0 à 1.5")

        CD = float(input("Coefficient de traînée (CD): "))
        if CD < 0:
            raise ValueError("Le coefficient de traînée ne peut pas être négatif")
        if CD > 0.5:
            print("⚠️  WARNING: CD très élevé")

        V_in = float(input("Vitesse d'intrusion axiale (m/s): "))
        if V_in < 0:
            raise ValueError("La vitesse axiale ne peut pas être négative")

        N = 10  # Nombre de segments de pale (discrétisation radiale)
        dr = R / N  # Largeur d'un segment radial

        T_total = 0
        Q_total = 0

        for i in range(N):
            # Position radiale au centre du segment (méthode des rectangles)
            r = (i + 0.5) * dr

            # Vitesse tangentielle : u = ω × r (augmente linéairement avec le rayon)
            u = omega * r

            # Vitesse résultante : combinaison vectorielle de u (tangentielle) et V_in (axiale)
            W = math.sqrt(u**2 + V_in**2)

            # Angle d'inclinaison du flux (inflow angle) : angle entre vitesse résultante et plan de rotation
            phi = math.atan(V_in / u)

            sin_phi = V_in / W
            cos_phi = u / W

            # Forces par unité de longueur selon les composantes axiale et tangentielle
            # Portance contribue à la poussée (composante axiale), traînée au couple (composante tangentielle)
            L_per_unit = 0.5 * rho * (W**2) * c * CL * sin_phi  # Contribution axiale de la portance
            D_per_unit = 0.5 * rho * (W**2) * c * CD * cos_phi  # Contribution tangentielle de la traînée

            # Intégration sur le segment radial : dT = force × nombre de pales × largeur radiale
            dT = B * L_per_unit * dr

            # Couple : force tangentielle × bras de levier (r) × largeur radiale
            dQ = B * D_per_unit * r * dr

            T_total += dT
            Q_total += dQ

        print(f"\nPoussée totale: {T_total:.2f} N")
        print(f"Couple total: {Q_total:.2f} Nm")

    except ValueError as e:
        print(f"\n❌ ERREUR: {e}")
        print("Veuillez entrer des valeurs numériques valides.")

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
