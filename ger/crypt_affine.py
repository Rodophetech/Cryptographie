#Script pour chiffrer et dechiifer avec Vigenere
import tkinter as tk
from tkinter import ttk
import string 
from tkinter import messagebox
state = 0

def on_valider_click():

    msg1 = msg.get("1.0", "end-1c")
    keya = key1.get() 
    keya2 = key2.get()

    if msg1 == "" or keya == "" or keya2 == "":
        messagebox.showerror("Erreur", "Les deux champs doivent être remplir ")

    else : 
        try:
            
            if state == 0:
                deja_chiffrer = chiffrement_affine(msg1, keya, keya2)
                res.insert("1.0",deja_chiffrer)
            else:
                deja2_chiffrer = dechiffrement_affine(msg1, keya, keya2)
                res.insert("1.0", "")
                res.insert("1.0",deja2_chiffrer)

        except:
            messagebox.showerror("Erreur", "Les valeurs a et b doivent être premier entre eux")
        
    

def modify(event):
    global choix
    global valider
    global state
    selected_value = choix.get()
    if selected_value == "Chiffrer":
        state = 0
    
    else:
        state = 1
    valider['text'] = selected_value
    print(state)

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def chiffrement_affine(texte, a, b):
    texte_chiffre = ""
    try:
        a = int(a)
        b = int(b)
        for caractere in texte:
            if caractere.isalpha():
                if caractere.isupper():
                        texte_chiffre += chr((a * (ord(caractere) - 65) + b) % 26 + 65)
                else:
                        texte_chiffre += chr((a * (ord(caractere) - 97) + b) % 26 + 97)
            else:
                texte_chiffre += caractere
    except: 
         print("Les veleurs doivent être premier entre eux")
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, a, b):
    a = int(a)
    b = int(b)
    a_inverse = mod_inverse(a, 26)
    texte_dechiffre = ""
    try:
        for caractere in texte_chiffre:
            if caractere.isalpha():
                if caractere.isupper():
                        texte_dechiffre += chr((a_inverse * (ord(caractere) - 65 - b)) % 26 + 65)
                else:
                        texte_dechiffre += chr((a_inverse * (ord(caractere) - 97 - b)) % 26 + 97)
            else:
                texte_dechiffre += caractere
    except:
        print("Les valeurs a et b doivent être premier entre eux")
    return texte_dechiffre
root = tk.Tk()
root.geometry("400x400")

root.resizable(False, False)
root.title("Chiffrer et dechiffrer avec Vigenere")
bg = "#2a9d8f"
root['bg'] = bg
tk.Label(root, text="Chiffrement Affine", font=("Arial", 18), bg=bg, fg="white").place(x=15, y=30)
tk.Label(root, text="Type", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=90)
options = ["Chiffrer", "Déchiffrer"]
choix = ttk.Combobox(root, values=options)
choix.place(x=150, y=90)
choix.current(0)
choix.bind('<<ComboboxSelected>>', modify)
tk.Label(root, text="Message", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=130)
msg = tk.Text(root, height=2, width=17)
msg.place(x=150, y=140)

tk.Label(root, text="Valeur a", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=200)
key1 = tk.Entry(root, width=23)
key1.place(x=150, y=205)

tk.Label(root, text="Valeur b", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=240)
key2 = tk.Entry(root, width=23)
key2.place(x=150, y=250)

tk.Label(root, text="Résultat", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=270)
res = tk.Text(root, height=2, width=17)
res.place(x=150, y=280)

valider = tk.Button(root, text="Chiffrer", activebackground=bg, width=11, bg=bg, font=("Arial", 16), fg="white",
                    command=on_valider_click)
valider.place(x=150, y=330)
root.mainloop()
