# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Script pour chiffrer et dechiifer avec Vigenere
import tkinter as tk
from subprocess import run 

def clik():
    run(["python", "cryp_2.py"])

def btn_poly():
    run(["python", "crypt1.py"])

def btn_affine():
    run(["python", "crypt_affine.py"])

root = tk.Tk()
root.geometry("500x400")
root.resizable(False, False)
root.title("Chiffrer et dechiffrer avec Vigenere")
bg = "#2a9d8f"
root['bg'] = bg
crypt_mono = tk.Button(root, text="Crytographie monoalphabetique", bg="#cfdbd5",
                       activebackground="#cfdbd5", fg="black", font=("Arial italic", 15), bd=0, width=28, command=clik)
crypt_mono.place(x=100, y=100)

crypt_poly = tk.Button(root, text="Crytographie polyalphabetique", bg="#cfdbd5",
                       fg="black",activebackground="#cfdbd5", font=("Arial italic", 15), bd=0, width=28, command=btn_poly)
crypt_poly.place(x=100, y=150)
crypt_afine = tk.Button(root, text="Crytographie affine", bg="#cfdbd5",
                       fg="black",activebackground="#cfdbd5", font=("Arial italic", 15), bd=0, width=28, command=btn_affine)
crypt_afine.place(x=100, y=200)

root.mainloop()
