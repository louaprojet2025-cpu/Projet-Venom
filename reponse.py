# Fichier : /venom_ai/reponse.py

# Pour l'instant, nous n'avons pas besoin d'imports complexes, 
# nous les ajouterons dans les prochaines tâches.

def generer_reponse_miroir(profil: dict) -> str:
    """
    Génère une réponse textuelle en mode miroir basée sur un profil de style.

    Args:
        profil (dict): Un dictionnaire contenant le profil de style de l'utilisateur.
                       Exemple: {'Richesse': 'Simple', 'Polarité': 'positive'}

    Returns:
        str: La réponse textuelle générée par l'IA.
    """
    
    # --- Tâche 2.2 (à venir) : Construire la directive (prompt) ---
    # Pour l'instant, on met un texte de remplacement.
    prompt_construit = f"ACTION EN ATTENTE : Construire le prompt pour un profil {profil}"
    print(f"[DEBUG] Prompt qui sera envoyé à l'IA : {prompt_construit}")

    # --- Tâche 2.3 (à venir) : Interroger le modèle de langage ---
    # Pour l'instant, on simule une réponse.
    reponse_generee = f"RÉPONSE SIMULÉE pour le profil {profil['Richesse']} et {profil['Polarité']}."

    return reponse_generee

# --- Section de Test ---
# Pour vérifier que notre fonction est bien structurée.
if __name__ == "__main__":
    print("--- Test du module de réponse v0.1 (squelette) ---")
    
    # On simule un profil de style que le module de perception nous aurait donné.
    profil_test = {'Richesse': 'Simple', 'Polarité': 'positive'}
    
    # On appelle notre nouvelle fonction avec ce profil.
    reponse_test = generer_reponse_miroir(profil_test)
    
    print(f"\nProfil d'entrée : {profil_test}")
    print(f"-> Réponse obtenue : {reponse_test}")
