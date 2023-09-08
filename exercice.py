#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    
    for i in range(len(mot)):
        mot=mot[:i]+ chr(ord(mot[i])-32) + mot[i+1:]
    return mot


if __name__ == '__main__':a
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
    

