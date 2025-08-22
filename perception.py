# Fichier : /venom_ai/perception.py

# On importe la "boîte à outils" de Hugging Face
from transformers import pipeline

# On initialise le modèle une seule fois. 
# C'est plus efficace que de le charger à chaque fois qu'on analyse une phrase.
try:
    analyseur_emotion = pipeline("sentiment-analysis", model="cmarkea/distilcamembert-base-sentiment")
except Exception as e:
    print(f"Erreur lors du chargement du modèle d'analyse d'émotion : {e}")
    # Si le modèle ne peut pas être chargé, on crée un analyseur "factice" pour éviter que le programme ne plante.
    analyseur_emotion = None

def analyser_polarite_emotionnelle(phrase: str) -> str:
    """
    Analyse une phrase et retourne sa polarité émotionnelle ('positive' ou 'negative').
    
    Args:
        phrase (str): La phrase à analyser.
        
    Returns:
        str: La polarité détectée.
    """
    if not isinstance(phrase, str) or not phrase.strip():
        return "indéterminée"

    if analyseur_emotion:
        try:
            resultat = analyseur_emotion(phrase)
            return resultat[0]['label']
        except Exception as e:
            print(f"Erreur lors de l'analyse de la phrase : {e}")
            return "erreur"
    
    return "non disponible"

# --- Section de Test ---
# Ce bloc de code ne s'exécute que si on lance ce fichier directement.
# Il nous permet de tester notre fonction sans affecter le reste du projet.
if __name__ == "__main__":
    print("--- Test du module de perception émotionnelle ---")
    
    phrase1 = "C'est une journée absolument magnifique !"
    emotion1 = analyser_polarite_emotionnelle(phrase1)
    print(f"Phrase : '{phrase1}'")
    print(f"-> Émotion détectée : {emotion1}\n")

    phrase2 = "Je suis vraiment déçu par ce résultat."
    emotion2 = analyser_polarite_emotionnelle(phrase2)
    print(f"Phrase : '{phrase2}'")
    print(f"-> Émotion détectée : {emotion2}\n")
