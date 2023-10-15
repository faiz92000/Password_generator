import random
import string

def generate_password(length=12, special_chars=True):
    # Caractères possibles pour le mot de passe
    characters = string.ascii_letters + string.digits
    if special_chars:
        characters += string.punctuation

    # Génération du mot de passe aléatoire
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    length = int(input("Longueur du mot de passe : "))
    special_chars = input("Inclure des caractères spéciaux ? (Oui/Non) : ").lower() in ["oui", "yes"]

    password = generate_password(length, special_chars)
    print("Mot de passe généré :", password)
