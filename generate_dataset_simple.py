# generate_dataset_simple.py

import pandas as pd
import random

# Configuration
NB_LIGNES = 300
PROVINCES = ["Agadir-Ida Ou Tanane", "Al Haouz", "Al Hoceïma", "Aousserd", "Assa-Zag", "Azilal", "Benslimane", "Berkane", "Berrechid", "Béni Mellal", "Boujdour", "Boulemane", "Casablanca", "Chefchaouen", "Chichaoua", "Chtouka Aït Baha", "Driouch", "El Hajeb", "El Jadida", "El Kelâa des Sraghna", "Errachidia", "Es-Semara", "Essaouira", "Fahs-Anjra", "Fès", "Figuig", "Fquih Ben Salah", "Guercif", "Guelmim", "Ifrane", "Inezgane-Aït Melloul", "Jerada", "Kénitra", "Khémisset", "Khénifra", "Khouribga", "Laâyoune", "Larache", "Marrakech", "Médiouna", "Meknès", "Midelt", "Mohammedia", "Moulay Yacoub", "M'Diq-Fnideq", "Nador", "Nouaceur", "Ouarzazate", "Oued Ed-Dahab", "Ouezzane", "Oujda-Angad", "Rabat", "Rehamna", "Safi", "Salé", "Settat", "Sefrou", "Sidi Bennour"]

def generer_chauffeur():
    province_res = random.choice(PROVINCES)
    province_dem = random.choice(PROVINCES)
    age = random.randint(18, 75)
    anciennete = random.randint(0, min(35, age-16))
    casier = random.choice([1, 1, 1, 1, 0])
    
    # Décision
    residence_ok = (province_res == province_dem)
    age_ok = (age <= 50)
    anciennete_ok = (anciennete >= 5)
    casier_ok = (casier == 1)
    
    decision = 1 if (residence_ok and age_ok and anciennete_ok and casier_ok) else 0
    
    return {
        'province_residence': province_res,
        'province_demandee': province_dem,
        'age': age,
        'anciennete_permis': anciennete,
        'casier_vierge': casier,
        'decision': decision
    }

# Génération
data = [generer_chauffeur() for _ in range(NB_LIGNES)]
df = pd.DataFrame(data)

# Sauvegarde
df.to_csv("dataset_permis_confiance.csv", index=False, encoding='utf-8')

print(f"✅ Dataset généré avec {len(df)} lignes")
print(f"📊 Taux d'acceptation : {df['decision'].mean()*100:.1f}%")
print(df.head())
