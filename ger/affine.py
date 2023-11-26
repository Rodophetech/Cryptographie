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

# Exemple d'utilisation
texte_clair = "Rodolphe aime le foot"
a = 5
b = 8

texte_chiffre = chiffrement_affine(texte_clair, a, b)
print("Texte chiffré:", texte_chiffre)

texte_dechiffre = dechiffrement_affine(texte_chiffre, a, b)
print("Texte déchiffré:", texte_dechiffre)

