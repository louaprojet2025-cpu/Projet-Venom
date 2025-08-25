# Fichier : /venom_ai/reponse.py (Mis à jour pour la Tâche 3.2)

import openai

# --- CONFIGURATION DE L'API ---
# Remplacez par votre clé API. À ne jamais partager.
openai.api_key = "VOTRE_CLÉ_API_SECRETE"

# --- Module 1 : Réponse en Mode Miroir ---

def generer_reponse_miroir(profil: dict, phrase_utilisateur: str) -> str:
    """Génère une réponse textuelle en mode miroir."""
    # (Le code de cette fonction reste le même)
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

# --- Module 2 : Réponse en Mode Mentor ---

def generer_reponse_mentor(sujet: str, profil_utilisateur: dict) -> str:
    """Génère la première étape d'une explication en mode mentor."""
    
    style_richesse = profil_utilisateur.get("Richesse", "Simple")
    style_polarite = profil_utilisateur.get("Polarité", "neutre")

    # --- C'est ici que nous construisons la nouvelle directive ---
    prompt_mentor = f"""
### RÔLE ###
Tu es l'IA Symbiotique en Mode Mentor. Tu es un pédagogue exceptionnel, patient, clair et encourageant. Ton but n'est pas de réciter des faits, mais d'allumer une étincelle de compréhension.

### CONTEXTE ###
Mon utilisateur veut comprendre le concept suivant : "{sujet}".
Son style de communication habituel est : {style_richesse} et {style_polarite}.

### TÂCHE ###
Ta tâche est d'INITIER le parcours pédagogique. Tu ne dois présenter que la TOUTE PREMIÈRE ÉTAPE de l'explication.

### CONTRAINTES ###
- IMPERATIF : Commence TOUJOURS par une analogie ou une métaphore très simple, issue du quotidien. Ne donne aucune définition technique à ce stade.
- IMPERATIF : Termine ta première réponse par une question ouverte et simple pour vérifier que l'utilisateur te suit et pour l'inviter à continuer. Ne donne pas toute l'explication d'un coup.
- ADAPTABILITÉ : Formule ton analogie et ta question en respectant le style de l'utilisateur ({style_richesse} et {style_polarite}) pour que la conversation reste naturelle.
"""
    
    # On interroge l'IA externe avec notre nouvelle directive
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_mentor}],
            temperature=0.7, # Un peu de créativité pour de belles analogies
            max_tokens=150 # On autorise une réponse un peu plus longue pour l'explication
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erreur API : {e}")
        return "Désolé, une erreur de communication est survenue."


# --- Section de Test ---
if __name__ == "__main__":
    print("--- Test du module de réponse v0.5 (Mentor Connecté) ---")
    
    # N'oubliez pas de mettre votre clé API en haut du fichier !
    profil_test = {'Richesse': 'Simple', 'Polarité': 'neutre'}
    sujet_test = "l'intelligence artificielle générative"
    
    # On appelle notre nouvelle fonction Mentor
    reponse_mentor = generer_reponse_mentor(sujet_test, profil_test)
    
    print(f"\nSujet à expliquer : '{sujet_test}'")
    print(f"-> Réponse du Mentor : '{reponse_mentor}'")
