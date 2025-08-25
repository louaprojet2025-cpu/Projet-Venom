# Fichier : /main.py (Le Cerveau du Projet Venom)

# On importe les fonctions de nos modules que nous avons construits
from venom_ai.perception import generer_profil_style
from venom_ai.reponse import generer_reponse_miroir, generer_reponse_mentor

# --- Le Cerveau de Décision : Le Méta-Contrôleur ---

# On définit la liste des mots-clés qui vont déclencher le Mode Mentor
DECLENCHEURS_MENTOR = [
    "c'est quoi", "explique-moi", "je comprends pas", "qu'est-ce que",
    "comment ça marche", "peux-tu m'expliquer", "c'est quoi le concept"
]

def extraire_sujet(phrase: str) -> str:
    """Extrait le sujet d'une question pour le Mode Mentor."""
    for declencheur in DECLENCHEURS_MENTOR:
        if declencheur in phrase:
            # On retourne la partie de la phrase qui vient APRÈS le déclencheur
            return phrase.split(declencheur, 1)[1].strip()
    return "ce concept" # Sujet par défaut si on ne trouve pas

# --- Le Flux de Conversation Principal ---

def converser_avec_venom():
    """Lance une session de conversation interactive avec l'IA Symbiotique."""
    print("--- IA Symbiotique (Projet Venom) v1.0 activée ---")
    print("Vous pouvez commencer à discuter. Tapez 'quitter' pour terminer.")
    
    while True:
        # 1. On récupère la phrase de l'utilisateur
        phrase_utilisateur = input("\nVous : ")
        if phrase_utilisateur.lower() == 'quitter':
            print("\n--- IA Symbiotique désactivée ---")
            break

        # 2. Le Module de Perception analyse le style
        profil = generer_profil_style(phrase_utilisateur)
        print(f"[DEBUG] Profil perçu : {profil}")

        # 3. Le Méta-Contrôleur DÉCIDE du mode
        phrase_lower = phrase_utilisateur.lower()
        mode_choisi = "Miroir" # Mode par défaut
        for declencheur in DECLENCHEURS_MENTOR:
            if declencheur in phrase_lower:
                mode_choisi = "Mentor"
                break
        
        print(f"[DEBUG] Décision du Méta-Contrôleur -> Mode : {mode_choisi}")
        
        # 4. On appelle le module de réponse approprié
        if mode_choisi == "Mentor":
            sujet = extraire_sujet(phrase_lower)
            reponse_finale = generer_reponse_mentor(sujet, profil)
        else: # Si ce n'est pas Mentor, c'est Miroir
            reponse_finale = generer_reponse_miroir(profil, phrase_utilisateur)
            
        # 5. On affiche la réponse finale
        print(f"\nVenom : {reponse_finale}")

# --- Point de Lancement ---
if __name__ == "__main__":
    converser_avec_venom()
