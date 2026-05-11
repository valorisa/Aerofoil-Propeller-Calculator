# ⚠️ RÉSULTATS DE VALIDATION CRITIQUES

## Découverte Importante

Le script `validate_apc.py` a révélé une **erreur fondamentale** dans les formules utilisées par AeroDynaCalc.

### Formules Actuelles (INCORRECTES)

```python
omega = rpm * 2 * math.pi / 60  # Conversion RPM → rad/s
T = (CT * rho * (omega**2) * (D**4)) / 8
Q = (CQ * rho * (omega**2) * (D**5)) / 8
```

**Erreur constatée : 479%** (facteur ~4.8× trop élevé)

### Formules Correctes (Théorie Standard)

Les formules standard de la théorie de quantité de mouvement utilisent **n en révolutions/seconde (rps)**, pas ω en rad/s :

```python
n = rpm / 60  # Conversion RPM → rps (révolutions par seconde)
T = CT * rho * (n**2) * (D**4)
Q = CQ * rho * (n**2) * (D**5)
```

### Explication Mathématique

La confusion vient de deux conventions différentes :

**Convention 1 : avec n (rps)**
- T = CT × ρ × n² × D⁴
- Utilisée dans la littérature (McCormick, Leishman, APC)

**Convention 2 : avec ω (rad/s)**  
- T = CT' × ρ × ω² × D⁴
- Où CT' = CT / (2π)²  
- Moins courante, nécessite des coefficients différents

Le code actuel **mélange les deux conventions** : il utilise ω mais avec des CT/CQ calibrés pour n, et ajoute un facteur `/8` non documenté.

### Impact

**TOUTES les prédictions d'AeroDynaCalc sont incorrectes d'un facteur ~4.8×**

Cela confirme brutalement le verdict du conseil LLM :
> "Tant que vous n'avez pas cette preuve, votre repo est une fiction bien écrite."

### Action Requise

**OPTION A : Corriger les formules (RECOMMANDÉ)**
- Remplacer `omega` par `n = rpm / 60`
- Supprimer le `/8` non justifié
- Valider contre données APC

**OPTION B : Documenter les limites**
- Ajouter disclaimer massif dans le README
- Préciser "OUTIL PÉDAGOGIQUE UNIQUEMENT - NE PAS UTILISER POUR DIMENSIONNEMENT RÉEL"
- Retirer l'affirmation "erreur ~15-20%"

### Prochaines Étapes

1. Décider : corriger le code OU changer le positionnement (pédagogique vs utilisable)
2. Si correction : mettre à jour toutes les formules
3. Re-valider contre données APC
4. Mettre à jour README avec résultats de validation RÉELS

---

**Date de découverte** : 11 mai 2026  
**Découvert par** : Script de validation automatique `validate_apc.py`  
**Confirmé par** : Comparaison vs APC Performance Data
