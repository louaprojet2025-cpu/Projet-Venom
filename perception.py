# Fichier : /venom_ai/perception.py (Mis à jour pour la Tâche 3)

# --- Imports ---
from transformers import pipeline
import textstat # Notre nouvel import pour l'analyse lexicale

# --- Initialisation des Modèles ---
try:
    analyseur_emotion = pipeline("sentiment-analysis", model="cmarkea/distilcamembert-base-sentiment")
except Exception as e:
    print(f"Erreur chargement modèle émotion : {e}")
    analyseur_emotion = None

# On règle la langue pour l'analyse lexicale
textstat.set_lang('fr')

# --- Fonctions d'Analyse Spécifiques ---

def analyser_polarite_emotionnelle(phrase: str) -> str:
    """Analyse une phrase et retourne sa polarité émotionnelle ('positive' ou 'negative')."""
    if not isinstance(phrase, str) or not phrase.strip():
        return "indéterminée"
    if analyseur_emotion:
        try:
            resultat = analyseur_emotion(phrase)
            return resultat[0]['label']
        except Exception as e:
            print(f"Erreur analyse émotion : {e}")
            return "erreur"
    return "non disponible"

# NOUVEAU : Fonction pour l'analyse de la complexité lexicale
def analyser_richesse_lexicale(phrase: str) -> str:
    """Analyse une phrase et retourne sa richesse lexicale ('Simple' ou 'Élaboré')."""
    if not isinstance(phrase, str) or not phrase.strip():
        return "indéterminée"
    
    # On utilise le score de Flesch. Un score élevé signifie que c'est facile à lire.
    score_complexite = textstat.flesch_reading_ease(phrase)
    
    # On définit un seuil (60) pour décider si le style est simple ou élaboré.
    if score_complexite > 60:
        return "Simple"
    else:
        return "Élaboré"

# --- Fonction Unifiée (Cœur du Module) ---

def generer_profil_style(phrase: str) -> dict:
    """
    Génère le profil de style complet (Richesse + Polarité) pour une phrase donnée.
    C'est la fonction principale que le reste de notre IA utilisera.
    """
    polarite = analyser_polarite_emotionnelle(phrase)
    richesse = analyser_richesse_lexicale(phrase)
    
    profil = {
        "Richesse": richesse,
        "Polarité": polarite
    }
    return profil

# --- Section de Test ---
if __name__ == "__main__":
    print("--- Test du module de perception unifié (Émotion + Lexique) ---")
    
    phrase1 = "C'est une journée absolument magnifique !"
    profil1 = generer_profil_style(phrase1)
    print(f"Phrase : '{phrase1}'")
    print(f"-> Profil détecté : {profil1}\n")

    phrase2 = "La procrastination constitue un obstacle substantiel à la productivité."
    profil2 = generer_profil_style(phrase2)
    print(f"Phrase : '{phrase2}'")
    print(f"-> Profil détecté : {profil2}\n")

    phrase3 = "Je n'aime pas ça."
    profil3 = generer_profil_style(phrase3)
    print(f"Phrase : '{phrase3}'")
    print(f"-> Profil détecté : {profil3}\n")
