# AeroDynaCalc 🚀  
**Outil de calcul aérodynamique pour profils d'aile et hélices**

## 📌 Nom du dépôt suggéré  
  
*(Alternatives : voir 'repository-name-ideas.md' )*

## 📖 Description  
Ce projet propose un script Python interactif pour calculer des paramètres clés en aérodynamique :  
- Portance et traînée d'un profil d'aile.  
- Poussée et couple d'une hélice.  
- Nombre de Reynolds.  
- Méthode des éléments de pale (BEM) simplifiée.

## 🚀 Fonctionnalités  
1. **Calcul de la portance et traînée**  
   - Utilise les équations :
     ```math
      P = \frac{1}{2} \rho V^2 S C_P
     ```
     ```math
      T = \frac{1}{2} \rho V^2 S C_T 
     ```
     
2. **Calcul de la poussée et couple d'une hélice**  
   - Formules :
     ```math
     T = \frac{C_T \rho \omega^2 D^4}{8}
     ```
     ```math
     Q = \frac{C_Q \rho \omega^2 D^5}{8}
     ```
    
3. **Nombre de Reynolds**
   ```math
    Re = \frac{\rho V L}{\mu} \quad \text{ou} \quad Re = \frac{V L}{\nu}
   ```

4. **Méthode BEM simplifiée**
- Intègre la poussée et le couple via des éléments de pale.


## 📦 Structure du dépôt
```
Aerofoil-Propeller-Calculator/  
├── AeroDynaCalc.py      # Script principal  
├── README.md            # Ce fichier  
├── LICENSE              # Fichier de licence (ex. MIT)  
└── examples/            # Exemples d'entrées/sorties  
```

## 🎛️ Utilisation  
Le script propose un menu interactif :  


### Exemple de session :  


## 📝 Explications mathématiques  
### 1. **Théorie des aérofoils**  
- **Portance** : Force verticale due à la différence de pression ($C_P$).  
- **Traînée** : Résistance au mouvement ($C_T$).  

### 2. **Hélices**  
- **Poussée** : Résultante des portances locales sur les pales.  
- **Couple** : Effort de rotation induit par la traînée.  

### 3. **Méthode BEM**  
- **Équations clés** :
```math
  W = \sqrt{(u^2 + V_{in}^2)}
```
```math
  phi = \arctan\left(\frac{V_{in}}{u}\right)
```
```math
  dT = B \cdot L_{\text{par unité}} \cdot dr 
```

## 🤝 Contributions  
- **Améliorations souhaitées** :  
  - Ajout de profils NACA standardisés.  
  - Visualisation graphique des résultats (via ).  
  - Extension de la méthode BEM pour inclure l'effet de la compressibilité.  

- **Comment contribuer** :  
  1. Fork le dépôt.  
  2. Créez une branche (*new-branch*).  
  3. Validez les tests (à ajouter).  
  4. Soumettez une Pull Request.

## 📝 Licence  
Distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📌 Liens utiles  
- [Documentation Python](https://docs.python.org/3/)  
- [Ressources aérodynamiques](https://en.wikipedia.org/wiki/Aerodynamics)
