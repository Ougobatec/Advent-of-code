# Advent of Code - Solutions Python

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org)

Bienvenue sur mon dépôt GitHub de l'**Advent of Code** ! 🎄

Ce projet regroupe mes solutions aux défis de l'[Advent of Code](https://adventofcode.com/), écrites en Python. Chaque année, l'Advent of Code propose des énigmes quotidiennes durant le calendrier de l'Avent, avec une difficulté croissante. Ce dépôt centralise l'ensemble de mes solutions au fil des années.

## 🚀 Objectif

L'Advent of Code est un événement annuel de programmation se déroulant en décembre, avec des défis quotidiens qui deviennent de plus en plus difficiles. Chaque défi est divisé en deux parties : la première est généralement plus simple, tandis que la seconde demande une optimisation ou une approche plus poussée.

## 💻 Technologies

- Python

## 📂 Structure du dépôt

```
Advent-of-code/
│
├── .gitignore            # Configuration des fichiers à ignorer
├── README.md             # Documentation du projet
├── run.py                # Script utilitaire pour exécuter les solutions
├── setup.py              # Script pour générer automatiquement la structure
│
├── 2015/
│   ├── 01/
|   |   ├── solutions.py
|   |   └── input.txt
│   ├── 02/
|   |   ├── solutions.py
|   |   └── input.txt
│   └── ...
│
├── 2016/
│   ├── 01/
|   |   ├── solutions.py
|   |   └── input.txt
│   ├── 02/
|   |   ├── solutions.py
|   |   └── input.txt
│   └── ...
│
└── ...
```

Chaque année est contenue dans un répertoire `YYYY`, et chaque répertoire de jour (`n`) pour une année donnée contient :
- Le fichier Python `solutions.py` avec les deux solutions du jour (structure avec fonctions)
- Un fichier `input.txt` avec les données d'entrée pour résoudre le défi

### Structure des solutions

Les fichiers `solutions.py` suivent une structure avec des fonctions :

```python
def load_input():
    """Charge les données d'entrée."""
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]

def part1(data):
    """Résout la partie 1."""
    return 42  # Votre solution ici

def part2(data):
    """Résout la partie 2."""  
    return 84  # Votre solution ici

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
```

**Avantages de cette approche :**
- **Plus propre** : Séparation claire entre chargement des données et logique
- **Plus rapide** : Le script `run.py` importe et exécute directement les fonctions
- **Plus testable** : Fonctions isolées faciles à tester

## 🧩 Comment utiliser ce Dépôt

### Cloner le dépôt

```bash
git clone https://github.com/Ougobatec/Advent-of-code.git
cd Advent-of-code
```

### Générer la setup automatiquement

Pour créer automatiquement tous les dossiers et fichiers vides depuis 2015 jusqu'à l'année actuelle :

```bash
./setup.py
```

Ce script génère :
- Tous les dossiers `YYYY/DD/` pour chaque année depuis 2015
- Les fichiers `solutions.py` avec un template pré-rempli
- Les fichiers `input.txt` vides à remplir avec vos données
- Affiche les commandes utiles pour commencer

### Exécuter une solution

#### Méthode directe

```bash
python3 2015/01/solutions.py
```

#### Script utilitaire

Pour plus de commodité, vous pouvez utiliser le script `run.py` :

```bash
./run.py --latest            # Dernière solution implémentée
./run.py --list 2015         # Solutions implémentées pour 2015
./run.py 2015 1              # Jour 1 de 2015
```

## 📝 Notes importantes

### Fichiers d'entrée personnalisés (`input.txt`)

Les fichiers `input.txt` sont **exclus du versioning Git** car chaque utilisateur d'Advent of Code reçoit des données d'entrée personnalisées. Pour obtenir vos fichiers :

1. Connectez-vous sur [adventofcode.com](https://adventofcode.com)
2. Naviguez vers le jour souhaité (ex: [2015 Day 1](https://adventofcode.com/2015/day/1))
3. Téléchargez votre fichier d'entrée personnalisé
4. Placez-le dans le dossier correspondant (ex: `2015/01/input.txt`)

### Autres informations

- Le `.gitignore` exclut également les fichiers Python temporaires (`__pycache__/`, `*.pyc`) et les environnements virtuels (`.venv/`, `venv/`).
- Le script `setup.py` se met automatiquement à jour chaque année pour inclure la nouvelle année courante.
- Chaque fichier `solutions.py` contient un template pré-rempli avec les commentaires en français pour vous aider à démarrer.
- Les fichiers `setup.py` et `run.py` sont configurés comme exécutables dans Git. Si pour une raison quelconque ils ne le sont pas après clonage, utilisez `chmod +x setup.py run.py`.

## 🧑‍💻 À propos

L'Advent of Code est une excellente occasion de pratiquer la programmation, d'explorer des algorithmes et de relever des défis intéressants. Ce dépôt regroupe toutes mes solutions depuis 2015, en utilisant Python. Si vous êtes intéressé par la résolution de problèmes algorithmiques, n'hésitez pas à explorer ce dépôt !

Bonne chance et amusez-vous bien avec l'Advent of Code ! 🎉
