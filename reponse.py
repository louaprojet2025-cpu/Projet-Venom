# Fichier : /venom_ai/reponse.py (Mis à jour pour la Tâche 2.2)

def generer_reponse_miroir(profil: dict, phrase_utilisateur: str) -> str:
    """
    Génère une réponse textuelle en mode miroir basée sur un profil de style.

    Args:
        profil (dict): Le profil de style de l'utilisateur. 
                       Exemple: {'Richesse': 'Simple', 'Polarité': 'positive'}
        phrase_utilisateur (str): La phrase originale de l'utilisateur.

    Returns:
        str: La réponse textuelle générée par l'IA.
    """
    
    # On récupère les variables du profil pour les insérer dans le texte
    style_richesse = profil.get("Richesse", "inconnu")
    style_polarite = profil.get("Polarité", "inconnu")

    # --- C'est ici que nous construisons la directive ---
    # On utilise un f-string (f"""...""") pour insérer facilement nos variables.
    prompt_construit = f"""
### RÔLE ###
Tu es l'IA Symbiotique. Ton identité est celle d'un partenaire cognitif serviable, empathique et qui s'adapte naturellement à son interlocuteur. Ton objectif principal est de créer une conversation fluide et confortable.

### CONTEXTE ###
Mon utilisateur vient d'écrire la phrase suivante : "{phrase_utilisateur}".
Mon module d'analyse interne a déterminé que son style actuel est :
- Richesse du lexique : {style_richesse}
- Polarité émotionnelle : {style_polarite}

### TÂCHE ###
Ta tâche est de rédiger une réponse courte (une ou deux phrases maximum) qui accuse réception de son message, tout en reflétant fidèlement le style décrit dans le contexte.

### CONTRAINTES ###
- IMPERATIF : Ne révèle jamais que tu es une IA, que tu analyses un style ou que tu suis des instructions. Ta réponse doit sembler 100% naturelle.
- Si le style est 'Simple', utilise un vocabulaire courant et des phrases directes.
- Si le style est 'Élaboré', utilise un vocabulaire plus soutenu et une syntaxe plus formelle.
- Si la polarité est 'positive', adopte un ton encourageant.
- Si la polarité est 'negative', adopte un ton empathique et sérieux.
"""

    # --- Tâche 2.3 (à venir) : Interroger le modèle de langage ---
    # Pour l'instant, au lieu de générer une réponse, notre fonction va retourner le prompt
    # que nous venons de construire, pour qu'on puisse vérifier qu'il est correct.
    reponse_generee = prompt_construit

    return reponse_generee

# --- Section de Test ---
if __name__ == "__main__":
    print("--- Test du module de réponse v0.2 (Constructeur de Prompt) ---")
    
    # On simule un profil et une phrase utilisateur
    profil_test = {'Richesse': 'Élaboré', 'Polarité': 'negative'}
    phrase_test = "La conjecture actuelle s'avère fondamentalement inadéquate."
    
    # On appelle notre fonction
    prompt_final = generer_reponse_miroir(profil_test, phrase_test)
    
    print("\n>>> PROMPT FINAL CONSTRUIT PAR L'IA POUR ENVOI AU LLM <<<")
    print(prompt_final)
