import tkinter as tk
import random
import string
import pyperclip

# Fonction pour générer un mot de passe
def generate_password():
    # Récupérez les critères saisis par l'utilisateur
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()

    # Liste de caractères possibles pour le mot de passe
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits

    # Générez un mot de passe aléatoire avec la longueur spécifiée
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Affichez le mot de passe généré
    password_label.config(text="Mot de passe généré : " + password)

    # Copiez le mot de passe dans le presse-papiers
    pyperclip.copy(password)

# Créez une instance de la classe Tk
app = tk.Tk()

# Définissez le titre de la fenêtre principale
app.title("Générateur de Mot de Passe")

# Définissez la taille initiale de la fenêtre
app.geometry("400x250")

# Ajoutez un libellé pour expliquer le but du programme
label = tk.Label(app, text="Bienvenue dans le Générateur de Mot de Passe")
label.pack()

# Ajoutez un champ de texte pour la longueur du mot de passe
length_label = tk.Label(app, text="Longueur du mot de passe :")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

# Ajoutez des cases à cocher pour les critères du mot de passe
uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(app, text="Inclure des lettres majuscules", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(app, text="Inclure des chiffres", variable=digits_var)
digits_check.pack()

# Ajoutez un bouton pour générer le mot de passe
generate_button = tk.Button(app, text="Générer le mot de passe", command=generate_password)
generate_button.pack()

# Ajoutez un bouton pour copier le mot de passe dans le presse-papiers
copy_button = tk.Button(app, text="Copier dans le presse-papiers", command=lambda: pyperclip.copy(password_label.cget("text").split(" : ")[1]))
copy_button.pack()

# Ajoutez un libellé pour afficher le mot de passe généré
password_label = tk.Label(app, text="")
password_label.pack()

# Cela démarre la boucle principale de l'application
app.mainloop()
