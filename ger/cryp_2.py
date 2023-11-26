#Script pour chiffrer et dechiifer avec Vigenere
import tkinter as tk
from tkinter import ttk
import string 
from tkinter import messagebox
state = 0

def on_valider_click():

    msg1 = msg.get("1.0", "end-1c")
    keya = key1.get() 
    if msg1 == "" or keya == "":
        messagebox.showerror("Erreur", "Les deux champs doivent être remplir ")

    else : 
        try:
            keya = int(keya)
            if state == 0:
                deja_chiffrer = chiffrer(msg1, keya)
                res.insert("1.0",deja_chiffrer)
            else:
                deja2_chiffrer = dechiffrer(msg1, keya)
                res.insert("1.0", "")
                res.insert("1.0",deja2_chiffrer)

        except:
            messagebox.showerror("Erreur", "La clé doit être un chiffre")
        
    

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

def chiffrer(texte, decalage):
    texte_chiffre = ""
    decalage = int(decalage)
    for char in texte:
        if char.isalpha():
            if char.isupper():
                texte_chiffre += chr((ord(char) + decalage - 65) % 26 + 65)
            else:
                texte_chiffre += chr((ord(char) + decalage - ord('a')) % 26 + ord('a'))
        else:
            texte_chiffre += char

    return texte_chiffre

def dechiffrer(texte_chiffre, decalage):
    texte_dechiffre = ""

    for char in texte_chiffre:
        if char.isalpha():
            if char.isupper():
                texte_dechiffre += chr((ord(char) - decalage - ord('A')) % 26 + ord('A'))
            else:
                texte_dechiffre += chr((ord(char) - decalage - ord('a')) % 26 + ord('a'))
        else:
            texte_dechiffre += char

    return texte_dechiffre
root = tk.Tk()
root.geometry("400x400")

root.resizable(False, False)
root.title("Chiffrer et dechiffrer avec Vigenere")
bg = "#2a9d8f"
root['bg'] = bg
tk.Label(root, text="Cryptographie Monoalphabétique", font=("Arial", 18), bg=bg, fg="white").place(x=15, y=30)
tk.Label(root, text="Type", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=90)
options = ["Chiffrer", "Déchiffrer"]
choix = ttk.Combobox(root, values=options)
choix.place(x=150, y=90)
choix.current(0)
choix.bind('<<ComboboxSelected>>', modify)
tk.Label(root, text="Message", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=130)
msg = tk.Text(root, height=2, width=17)
msg.place(x=150, y=140)

tk.Label(root, text="Clé", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=200)
key1 = tk.Entry(root, width=23)
key1.place(x=150, y=200)

tk.Label(root, text="Résultat", font=("Arial", 16), bg=bg, fg="white").place(x=30, y=250)
res = tk.Text(root, height=2, width=17)
res.place(x=150, y=260)

valider = tk.Button(root, text="Chiffrer", activebackground=bg, width=11, bg=bg, font=("Arial", 16), fg="white",
                    command=on_valider_click)
valider.place(x=150, y=320)
root.mainloop()
