# permis.py - Formulaire utilisateur avec validation des champs

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# --- Configuration de la page ---
st.set_page_config(
    page_title="Permis de Confiance Taxi",
    page_icon="🚖",
    layout="centered"
)

# --- Titre principal ---
st.title("🚖 Demande de Permis de Confiance")
st.subheader("Formulaire d'évaluation du chauffeur")
st.divider()

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.header("📋 Informations")
    st.info("Remplissez tous les champs du formulaire pour vérifier l'éligibilité.")
    st.caption("🔒 Aucune donnée réelle n'est stockée")

# --- INITIALISATION DES VARIABLES DE SESSION ---
if 'form_valid' not in st.session_state:
    st.session_state.form_valid = True
if 'erreurs' not in st.session_state:
    st.session_state.erreurs = []

# --- FORMULAIRE PRINCIPAL ---
st.markdown("### 📝 Renseignez les informations du chauffeur")

# Création du formulaire
with st.form("formulaire_permis"):
    
    # --- 1. CHAMP PROVINCE ---
    st.markdown("#### 📍 1. Province")
    
    # Message d'erreur pour la province
    if 'erreur_province' in st.session_state and not st.session_state.form_valid:
        st.error("⚠️ Veuillez sélectionner une province valide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        province_residence = st.selectbox(
            "Province de résidence *",
            ["", "Agadir-Ida Ou Tanane", "Al Haouz", "Al Hoceïma", "Aousserd", "Assa-Zag", "Azilal", "Benslimane", "Berkane", "Berrechid", "Béni Mellal", "Boujdour", "Boulemane", "Casablanca", "Chefchaouen", "Chichaoua", "Chtouka Aït Baha", "Driouch", "El Hajeb", "El Jadida", "El Kelâa des Sraghna", "Errachidia", "Es-Semara", "Essaouira", "Fahs-Anjra", "Fès", "Figuig", "Fquih Ben Salah", "Guercif", "Guelmim", "Ifrane", "Inezgane-Aït Melloul", "Jerada", "Kénitra", "Khémisset", "Khénifra", "Khouribga", "Laâyoune", "Larache", "Marrakech", "Médiouna", "Meknès", "Midelt", "Mohammedia", "Moulay Yacoub", "M'Diq-Fnideq", "Nador", "Nouaceur", "Ouarzazate", "Oued Ed-Dahab", "Ouezzane", "Oujda-Angad", "Rabat", "Rehamna", "Safi", "Salé", "Settat", "Sefrou", "Sidi Bennour"],
            help="Province où habite le chauffeur"
        )
    
    with col2:
        province_demandee = st.selectbox(
            "Province demandée *",
            ["","Agadir-Ida Ou Tanane", "Al Haouz", "Al Hoceïma", "Aousserd", "Assa-Zag", "Azilal", "Benslimane", "Berkane", "Berrechid", "Béni Mellal", "Boujdour", "Boulemane", "Casablanca", "Chefchaouen", "Chichaoua", "Chtouka Aït Baha", "Driouch", "El Hajeb", "El Jadida", "El Kelâa des Sraghna", "Errachidia", "Es-Semara", "Essaouira", "Fahs-Anjra", "Fès", "Figuig", "Fquih Ben Salah", "Guercif", "Guelmim", "Ifrane", "Inezgane-Aït Melloul", "Jerada", "Kénitra", "Khémisset", "Khénifra", "Khouribga", "Laâyoune", "Larache", "Marrakech", "Médiouna", "Meknès", "Midelt", "Mohammedia", "Moulay Yacoub", "M'Diq-Fnideq", "Nador", "Nouaceur", "Ouarzazate", "Oued Ed-Dahab", "Ouezzane", "Oujda-Angad", "Rabat", "Rehamna", "Safi", "Salé", "Settat", "Sefrou", "Sidi Bennour"],
            help="Province où le chauffeur souhaite exercer"
        )
    
    st.caption("⚠️ La province de résidence doit être identique à la province demandée")
    
    # --- 2. CHAMP ÂGE ---
    st.markdown("#### 🎂 2. Âge")
    
    # Message d'erreur pour l'âge
    if 'erreur_age' in st.session_state and not st.session_state.form_valid:
        st.error("⚠️ L'âge doit être compris entre 18 et 75 ans")
    
    age = st.number_input(
        "Âge du chauffeur *",
        min_value=18,
        max_value=75,
        value=35,
        step=1,
        help="Ne doit pas dépasser 50 ans"
    )
    
    # Affichage du statut
    if age > 50:
        st.error(f"❌ Âge {age} ans dépasse la limite de 50 ans")
    else:
        st.success(f"✅ Âge {age} ans (limite : 50 ans)")
    
    # --- 3. CHAMP PERMIS (ancienneté) ---
    st.markdown("#### 🪪 3. Permis de conduire")
    
    # Message d'erreur pour le permis
    if 'erreur_permis' in st.session_state and not st.session_state.form_valid:
        st.error("⚠️ Veuillez sélectionner une date d'obtention du permis valide")
    
    col3, col4 = st.columns(2)
    
    with col3:
        date_permis = st.date_input(
            "Date d'obtention du permis *",
            value=datetime.now() - timedelta(days=365*8),
            max_value=datetime.now(),
            min_value=datetime(1960, 1, 1),
            help="Date de délivrance du permis de conduire"
        )
    
    with col4:
        # Calcul de l'ancienneté
        aujourdhui = datetime.now().date()
        anciennete = (aujourdhui - date_permis).days // 365
        
        st.metric(
            "Ancienneté du permis",
            f"{anciennete} ans",
            delta="Minimum 5 ans" if anciennete < 5 else "✅ OK",
            delta_color="inverse" if anciennete < 5 else "normal"
        )
        
        if anciennete < 5:
            st.error(f"❌ Ancienneté {anciennete} ans inférieure à 5 ans")
        else:
            st.success(f"✅ Ancienneté {anciennete} ans (minimum : 5 ans)")
    
    # --- 4. CHAMP CASIER JUDICIAIRE ---
    st.markdown("#### ⚖️ 4. Casier judiciaire")
    
    # Message d'erreur pour le casier
    if 'erreur_casier' in st.session_state and not st.session_state.form_valid:
        st.error("⚠️ Veuillez sélectionner le statut du casier judiciaire")
    
    casier_vierge = st.radio(
        "Extrait du casier judiciaire (bulletin n°3) *",
        options=["", "✅ Oui, mention 'Néant'", "❌ Non, comporte des mentions"],
        help="Doit impérativement porter la mention 'Néant'",
        index=0
    )
    
    if casier_vierge == "✅ Oui, mention 'Néant'":
        st.success("✅ Casier judiciaire vierge")
    elif casier_vierge == "❌ Non, comporte des mentions":
        st.error("❌ Casier judiciaire non vierge")
    else:
        st.info("ℹ️ Veuillez sélectionner une option")
    
    # --- BOUTON DE SOUMISSION ---
    st.divider()
    
    col5, col6, col7 = st.columns([1, 2, 1])
    with col6:
        submitted = st.form_submit_button(
            "🔍 VÉRIFIER L'ÉLIGIBILITÉ",
            use_container_width=True,
            type="primary"
        )

# --- FONCTION DE VALIDATION DES CHAMPS ---
def valider_champs(province_res, province_dem, age_val, date_permis_val, casier_val):
    """
    Valide que tous les champs sont correctement remplis
    Retourne : (valid, liste_erreurs)
    """
    erreurs = []
    
    # 1. Vérification des provinces
    if not province_res or province_res == "":
        erreurs.append("❌ Veuillez sélectionner une province de résidence")
        st.session_state.erreur_province = True
    else:
        st.session_state.erreur_province = False
    
    if not province_dem or province_dem == "":
        erreurs.append("❌ Veuillez sélectionner une province demandée")
        st.session_state.erreur_province = True
    else:
        st.session_state.erreur_province = False
    
    if province_res == province_dem and province_res != "":
        # OK
        pass
    
    # 2. Vérification de l'âge
    if age_val < 18 or age_val > 75:
        erreurs.append("❌ L'âge doit être compris entre 18 et 75 ans")
        st.session_state.erreur_age = True
    else:
        st.session_state.erreur_age = False
    
    # 3. Vérification de la date du permis
    if not date_permis_val:
        erreurs.append("❌ Veuillez sélectionner une date d'obtention du permis")
        st.session_state.erreur_permis = True
    else:
        st.session_state.erreur_permis = False
    
    # 4. Vérification du casier
    if not casier_val or casier_val == "":
        erreurs.append("❌ Veuillez sélectionner le statut du casier judiciaire")
        st.session_state.erreur_casier = True
    else:
        st.session_state.erreur_casier = False
    
    # 5. Vérification supplémentaire : âge minimum pour conduire
    if age_val < 18:
        erreurs.append("❌ L'âge minimum pour conduire est de 18 ans")
    
    # 6. Vérification supplémentaire : ancienneté cohérente
    if date_permis_val:
        if anciennete > (age_val - 16):
            # Un conducteur ne peut pas avoir son permis avant 16-18 ans
            # On ne bloque pas mais on avertit
            pass
    
    # 7. Vérification des champs vides (message générique)
    champs_vides = []
    if province_res == "":
        champs_vides.append("Province de résidence")
    if province_dem == "":
        champs_vides.append("Province demandée")
    if casier_val == "":
        champs_vides.append("Casier judiciaire")
    
    if champs_vides:
        champs_str = ", ".join(champs_vides)
        erreurs.append(f"⚠️ Veuillez remplir les champs suivants : {champs_str}")
    
    # Déterminer si tout est valide
    valid = len(erreurs) == 0
    
    # Stocker les erreurs dans la session
    st.session_state.erreurs = erreurs
    st.session_state.form_valid = valid
    
    return valid, erreurs

# --- FONCTION DE GÉNÉRATION DU NUMÉRO DE PERMIS ---
def generer_numero_permis(province, age):
    """
    Génère un numéro de permis unique formaté
    Format : PC-YYYY-NNNN
    """
    annee = datetime.now().year
    numero = str(random.randint(1000, 9999))
    return f"PC-{annee}-{numero}"

# --- TRAITEMENT DU FORMULAIRE SOUMIS ---
if submitted:
    # --- ÉTAPE 1 : VALIDATION DES CHAMPS ---
    valid, erreurs = valider_champs(
        province_residence,
        province_demandee,
        age,
        date_permis,
        casier_vierge
    )
    
    # Si les champs ne sont pas valides, on affiche les erreurs et on arrête
    if not valid:
        st.divider()
        st.markdown("### ⚠️ Formulaire incomplet")
        st.error("**Veuillez corriger les erreurs suivantes :**")
        
        # Affichage des erreurs
        for erreur in erreurs:
            st.warning(erreur)
        
        # Aide supplémentaire
        st.markdown("---")
        st.markdown("#### 📌 Comment corriger :")
        
        if "province" in " ".join(erreurs).lower():
            st.write("- 📍 Sélectionnez une province valide dans les listes déroulantes")
        if "âge" in " ".join(erreurs).lower() or "age" in " ".join(erreurs).lower():
            st.write("- 🎂 Entrez un âge entre 18 et 75 ans")
        if "permis" in " ".join(erreurs).lower() or "date" in " ".join(erreurs).lower():
            st.write("- 🪪 Sélectionnez une date d'obtention du permis valide")
        if "casier" in " ".join(erreurs).lower():
            st.write("- ⚖️ Sélectionnez le statut du casier judiciaire")
        
        st.stop()  # Arrêter l'exécution ici
    
    # --- ÉTAPE 2 : TRAITEMENT SI TOUT EST VALIDE ---
    # Réinitialiser les erreurs de session
    st.session_state.form_valid = True
    st.session_state.erreurs = []
    
    st.divider()
    st.markdown("### 📊 Résultat de l'évaluation")
    
    # --- VÉRIFICATION DES 4 CRITÈRES ---
    
    # Critère 1 : Résidence correcte ?
    residence_ok = (province_residence == province_demandee)
    
    # Critère 2 : Âge correct ?
    age_ok = (age <= 50)
    
    # Critère 3 : Ancienneté correcte ?
    anciennete_ok = (anciennete >= 5)
    
    # Critère 4 : Casier vierge ?
    casier_ok = (casier_vierge == "✅ Oui, mention 'Néant'")
    
    # --- DÉCISION FINALE (TOUT DOIT ÊTRE OK) ---
    decision = (residence_ok and age_ok and anciennete_ok and casier_ok)
    
    # --- AFFICHAGE DU RÉSULTAT ---
    if decision:
        # ✅ PERMIS ACCORDÉ
        st.success("🎉 **PERMIS DE CONFIANCE ACCORDÉ !**")
        
        st.markdown("""
        Félicitations ! Le chauffeur remplit **tous les critères** requis.
        """)
        
        # --- GÉNÉRATION DU NUMÉRO DE PERMIS ---
        numero_permis = generer_numero_permis(province_demandee, age)
        date_delivrance = datetime.now().strftime("%d/%m/%Y")
        heure_delivrance = datetime.now().strftime("%H:%M:%S")
        
        # Affichage du numéro de permis en évidence
        st.markdown("📜 NUMÉRO DE PERMIS")
        st.markdown(f"**{numero_permis}**")
        st.markdown(f"Délivré le {date_delivrance}")
        # --- CRITÈRES VALIDÉS ---
        st.markdown("---")
        st.markdown("#### ✅ Critères validés :")
        
        col_valid1, col_valid2 = st.columns(2)
        with col_valid1:
            st.markdown(f"""
            - ✅ Province de résidence = Province demandée  
              *(Résidence : {province_residence} = Demandée : {province_demandee})*
            - ✅ Âge ≤ 50 ans  
              *({age} ans ≤ 50 ans)*
            """)
        with col_valid2:
            st.markdown(f"""
            - ✅ Ancienneté du permis ≥ 5 ans  
              *({anciennete} ans ≥ 5 ans)*
            - ✅ Casier judiciaire vierge  
              *(Mention « Néant »)*
            """)
        
        # --- DATE ET HEURE DE DÉLIVRANCE ---
        st.caption(f"📌 Permis délivré le {date_delivrance} à {heure_delivrance}")
        st.info("📄 L'attestation est disponible sur demande auprès de l'administration")
    else:
        # ❌ PERMIS REFUSÉ
        st.error("❌ **PERMIS DE CONFIANCE REFUSÉ**")
        
        # Date et heure du refus
        date_refus = datetime.now().strftime("%d/%m/%Y")
        heure_refus = datetime.now().strftime("%H:%M:%S")
        
        # --- COLLECTION DES MOTIFS DE REFUS ---
        motifs = []
        
        if not residence_ok:
            motifs.append(f"❌ Province de résidence ({province_residence}) différente de la province demandée ({province_demandee})")
        
        if not age_ok:
            motifs.append(f"❌ Âge ({age} ans) supérieur à 50 ans")
        
        if not anciennete_ok:
            motifs.append(f"❌ Ancienneté du permis ({anciennete} ans) inférieure à 5 ans")
        
        if not casier_ok:
            motifs.append("❌ Casier judiciaire non vierge")
        
        # Affichage des motifs
        st.markdown("#### 🚫 Motifs du refus :")
        for i, motif in enumerate(motifs, 1):
            st.write(f"{i}. {motif}")
        
        # --- RECOMMANDATIONS ---
        st.markdown("#### 💡 Recommandations :")
        
        if not age_ok:
            st.write(f"- ⏳ Attendre d'avoir **50 ans ou moins** (actuellement {age} ans)")
        
        if not anciennete_ok:
            st.write(f"- ⏳ Attendre **{5 - anciennete} ans** supplémentaires pour atteindre 5 ans d'ancienneté")
        
        if not residence_ok:
            st.write(f"- 📍 Faire la demande dans **{province_residence}** ou déménager à **{province_demandee}**")
        
        if not casier_ok:
            st.write("- ⚖️ Régulariser la situation judiciaire avant de refaire la demande")
        
        # --- NUMÉRO DE DOSSIER DE REFUS ---
        numero_dossier = f"REF-{datetime.now().strftime('%Y%m%d')}-{random.randint(100, 999)}"
        st.warning(f"📋 Numéro de dossier de refus : {numero_dossier}")
        st.caption(f"📌 Décision prise le {date_refus} à {heure_refus}")
    
    # --- AFFICHAGE DU TABLEAU RÉCAPITULATIF ---
    st.divider()
    with st.expander("📋 Voir le récapitulatif détaillé"):
        
        # Création des données pour le tableau
        tableau = {
            "Critère": ["Province de résidence", "Province demandée", "Âge", "Ancienneté du permis", "Casier judiciaire"],
            "Valeur": [
                province_residence,
                province_demandee,
                f"{age} ans",
                f"{anciennete} ans",
                "Vierge (Néant)" if casier_ok else "Non vierge"
            ],
            "Condition": [
                "= Province demandée",
                "= Province de résidence",
                "≤ 50 ans",
                "≥ 5 ans",
                "Mention 'Néant'"
            ],
            "Statut": [
                "✅ OK" if residence_ok else "❌ KO",
                "✅ OK" if province_demandee == province_residence else "❌ KO",
                "✅ OK" if age_ok else "❌ KO",
                "✅ OK" if anciennete_ok else "❌ KO",
                "✅ OK" if casier_ok else "❌ KO"
            ]
        }
        
        # Affichage du tableau
        col_t1, col_t2 = st.columns([2, 1])
        with col_t1:
            st.dataframe(tableau, use_container_width=True)
        
        with col_t2:
            st.metric(
                "Décision finale",
                "✅ ACCORDÉ" if decision else "❌ REFUSÉ",
                delta="Tous les critères sont remplis" if decision else "Au moins un critère non rempli",
                delta_color="normal" if decision else "inverse"
            )

# --- STATISTIQUES DE SESSION ---
if 'nb_tests' not in st.session_state:
    st.session_state.nb_tests = 0

if submitted and st.session_state.form_valid:
    st.session_state.nb_tests += 1

# Affichage dans la barre latérale
with st.sidebar:
    st.divider()
    st.success("Système automatisé de décision")
    st.info("Version prototype - Stage d'initiation")
    st.metric("📊 Simulations effectuées", st.session_state.nb_tests)
    st.caption(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    
    if st.button("🔄 Réinitialiser les statistiques"):
        st.session_state.nb_tests = 0
        st.rerun()

# --- CHARGEMENT DU DATASET CSV ---
@st.cache_data
def charger_dataset():
    """
    Charge le dataset CSV avec mise en cache
    """
    try:
        df = pd.read_csv("dataset_permis_confiance.csv", encoding='utf-8')
        return df
    except FileNotFoundError:
        st.warning("⚠️ Fichier 'dataset_permis_confiance.csv' non trouvé")
        return None
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement : {e}")
        return None

# --- AFFICHAGE DU DATASET ---
st.divider()
st.header("📊 Visualisation du dataset")

df = charger_dataset()

if df is not None:
    # --- FILTRES ---
    st.subheader("🔍 Filtrer les données")
    
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    
    with col_f1:
        decision_filter = st.multiselect(
            "Décision",
            options=[1, 0],
            format_func=lambda x: "✅ Accordé" if x == 1 else "❌ Refusé",
            default=[1, 0]
        )
    
    with col_f2:
        provinces = sorted(df['province_residence'].unique())
        province_filter = st.multiselect(
            "Province de résidence",
            options=provinces,
            default=provinces[:3] if len(provinces) > 3 else provinces
        )
    
    with col_f3:
        age_min = int(df['age'].min())
        age_max = int(df['age'].max())
        age_range = st.slider(
            "Tranche d'âge",
            min_value=age_min,
            max_value=age_max,
            value=(age_min, age_max)
        )
    
    with col_f4:
        casier_filter = st.multiselect(
            "Casier judiciaire",
            options=[1, 0],
            format_func=lambda x: "✅ Vierge" if x == 1 else "❌ Non vierge",
            default=[1, 0]
        )
    
    # --- APPLICATION DES FILTRES ---
    df_filtre = df[
        (df['decision'].isin(decision_filter)) &
        (df['province_residence'].isin(province_filter)) &
        (df['age'].between(age_range[0], age_range[1])) &
        (df['casier_vierge'].isin(casier_filter))
    ]
    
    st.divider()
    
    # --- AFFICHAGE DES DONNÉES ---
    st.subheader(f"📋 Données ({len(df_filtre)} lignes)")
    
    st.dataframe(
        df_filtre,
        use_container_width=True,
        height=400
    )
    
    # --- BOUTON DE TÉLÉCHARGEMENT ---
    csv = df_filtre.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Télécharger le CSV filtré",
        data=csv,
        file_name="dataset_filtre.csv",
        mime="text/csv",
        use_container_width=True
    )

else:
    st.info("💡 Aucun dataset chargé. Générez d'abord le fichier dataset_permis_confiance.csv")
# --- PIED DE PAGE ---
st.divider()
st.caption("🚖 Prototype de démonstration - Données fictives - Non contractuel")
st.caption("🔐 Aucune donnée personnelle n'est stockée")
st.caption(f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
