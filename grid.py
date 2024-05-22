import customtkinter as ctk

# Initialisation de la fenêtre principale
root = ctk.CTk()
root.geometry("400x300")

# Création de widgets
label1 = ctk.CTkLabel(master=root, text="Label 1", fg_color="red")
label2 = ctk.CTkLabel(master=root, text="Label 2", fg_color="green")
label3 = ctk.CTkLabel(master=root, text="Label 3", fg_color="blue")
label4 = ctk.CTkLabel(master=root, text="Label 4", fg_color="light blue")

# Placement des widgets dans la grille avec différentes valeurs de sticky
label1.grid(row=0, column=0, sticky="N")  # Collé au bord supérieur
label2.grid(row=0, column=1, sticky="E")  # Collé au bord droit
label3.grid(row=1, column=0, sticky="W")  # Collé au bord gauche
label4.grid(row=1, column=1, sticky="NSEW")  # Remplit toute la cellule

# Configuration de la grille pour permettre l'expansion
# root.grid_rowconfigure(0, weight=2)
# root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Lancement de la boucle principale
root.mainloop()