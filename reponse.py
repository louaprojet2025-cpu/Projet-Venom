# Fichier : /venom_ai/reponse.py (Mis à jour pour la Tâche 2.3)

import openai # On importe la bibliothèque pour communiquer avec l'IA externe

# --- CONFIGURATION DE L'API ---
# IMPORTANT : Remplacez "VOTRE_CLÉ_API_SECRETE" par votre propre clé.
# NE JAMAIS PARTAGER CETTE CLÉ PUBLIQUEMENT (par exemple sur GitHub).
openai.api_key = "VOTRE_CLÉ_API_SECRETE"

def generer_reponse_miroir(profil: dict, phrase_utilisateur: str) -> str:
    """
    Génère une réponse textuelle en mode miroir en interrogeant une IA externe.
    """
    style_richesse = profil.get("Richesse", "inconnu")
    style_polarite = profil.get("Polarité", "inconnu")

    # Étape 1 : On construit la directive (Tâche 2.2)
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

    # Étape 2 : On interroge l'IA externe (la nouveauté !)
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", # On choisit un modèle rapide et efficace
            messages=[
                {"role": "system", "content": "Tu es une IA assistante qui suit les instructions à la lettre."},
                {"role": "user", "content": prompt_construit}
            ],
            temperature=0.7, # Un peu de créativité, mais pas trop
            max_tokens=50 # Pour garder la réponse courte
        )
        reponse_generee = response.choices[0].message.content
        return reponse_generee
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API OpenAI : {e}")
        return "Désolé, une erreur de communication est survenue."

# --- Section de Test ---
if __name__ == "__main__":
    print("--- Test du module de réponse v0.3 (Connecté à l'IA externe) ---")
    
    # On simule un profil et une phrase utilisateur
    # N'oubliez pas de mettre votre clé API en haut du fichier !
    profil_test = {'Richesse': 'Simple', 'Polarité': 'positive'}
    phrase_test = "J'ai enfin fini ce rapport, je suis soulagé !"
    
    # On appelle notre fonction
    reponse_finale = generer_reponse_miroir(profil_test, phrase_test)
    
    print(f"\nUtilisateur a dit : '{phrase_test}'")
    print(f"-> Venom (IA Symbiotique) répond : '{reponse_finale}'")
