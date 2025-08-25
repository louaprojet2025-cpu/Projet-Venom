# Fichier : /venom_ai/reponse.py (Mis à jour pour la Tâche 3.1)

import openai

# --- CONFIGURATION DE L'API ---
# Remplacez par votre clé API. À ne jamais partager.
openai.api_key = "VOTRE_CLÉ_API_SECRETE"

# --- Module 1 : Réponse en Mode Miroir ---

def generer_reponse_miroir(profil: dict, phrase_utilisateur: str) -> str:
    """Génère une réponse textuelle en mode miroir en interrogeant une IA externe."""
    style_richesse = profil.get("Richesse", "inconnu")
    style_polarite = profil.get("Polarité", "inconnu")

    prompt_construit = f"""
### RÔLE ###
Tu es l'IA Symbiotique, un partenaire cognitif empathique et adaptatif.

### CONTEXTE ###
Mon utilisateur a écrit : "{phrase_utilisateur}". Son style est : {style_richesse} et {style_polarite}.

### TÂCHE ###
Rédige une courte réponse (1-2 phrases) qui reflète fidèlement ce style.

### CONTRAINTES ###
- Sois naturel et ne révèle jamais ton mécanisme interne.
- Adapte ton vocabulaire et ton ton au style fourni.
"""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_construit}],
            temperature=0.7,
            max_tokens=50
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erreur API : {e}")
        return "Désolé, une erreur de communication est survenue."

# --- NOUVEAU : Module 2 : Réponse en Mode Mentor ---

def generer_reponse_mentor(sujet: str, profil_utilisateur: dict) -> str:
    """
    Génère la première étape d'une explication en mode mentor.

    Args:
        sujet (str): Le concept que l'utilisateur veut comprendre.
        profil_utilisateur (dict): Le profil de style de l'utilisateur pour adapter le ton.

    Returns:
        str: La première réponse générée par l'IA en mode mentor.
    """
    
    # Tâche 3.2 (à venir) : Nous construirons le prompt du mentor ici.
    prompt_mentor = f"ACTION EN ATTENTE : Construire le prompt du Mentor pour le sujet '{sujet}'."
    print(f"[DEBUG] Prompt à construire : {prompt_mentor}")

    # Pour l'instant, on simule une réponse.
    reponse_simulee = f"RÉPONSE MENTOR SIMULÉE pour expliquer '{sujet}'."
    
    return reponse_simulee

# --- Section de Test ---
if __name__ == "__main__":
    print("--- Test du module de réponse v0.4 (Miroir + Squelette Mentor) ---")
    
    # 1. Test du Mode Miroir (inchangé)
    profil_miroir = {'Richesse': 'Simple', 'Polarité': 'positive'}
    phrase_miroir = "C'est une super nouvelle !"
    # reponse_miroir = generer_reponse_miroir(profil_miroir, phrase_miroir) # On le met en commentaire pour ne pas utiliser l'API à chaque test
    # print(f"\nTest Miroir -> Réponse obtenue : '{reponse_miroir}'")
    
    # 2. Test du nouveau squelette Mentor
    profil_mentor = {'Richesse': 'Simple', 'Polarité': 'negative'} # Le mentor doit s'adapter même si l'utilisateur est négatif
    sujet_mentor = "la physique quantique"
    reponse_mentor = generer_reponse_mentor(sujet_mentor, profil_mentor)
    print(f"\nTest Mentor -> Sujet demandé : '{sujet_mentor}'")
    print(f"-> Réponse obtenue : '{reponse_mentor}'")
