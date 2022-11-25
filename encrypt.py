#coding:utf-8
import unittest
def cle_cryptage(texte,cle):
    cle_chiffrement=''
    i = 0
    for caractere in texte:     # pour chaque caractère contenu dans le texte
        if caractere.isalpha():  # si le caractère est une lettre de l'alphabet
            cle_chiffrement += cle[i % len(cle)]
            i +=1
        else:
            cle_chiffrement += ' '
    return cle_chiffrement

def cryptage_lettre(texte_char, cle_char):
    if texte_char.isalpha():
        premiere_lettre='a'
        if texte_char.isupper():
            premiere_lettre='A'
        derniere_position_char = ord(texte_char) - ord(premiere_lettre)
        position_caractere_cle=ord(cle_char.lower()) - ord('a')
        nouvelle_position_char = (derniere_position_char + position_caractere_cle) %26
        return chr(nouvelle_position_char + ord(premiere_lettre))
    return texte_char


def cryptage(texte, cle):
    texte_à_chiffre=''
    cle_chiffrement=cle_cryptage(texte, cle)
    for texte_char, cle_char in zip(texte, cle_chiffrement):
        texte_à_chiffre += cryptage_lettre(texte_char, cle_char)
    return texte_à_chiffre

texte=input("Entrez le texte en clair : ")
key=input("Entrez la clé : ")

texte_à_chiffre= cryptage(texte, key)

print(f'Le message crypté est : {texte_à_chiffre}')