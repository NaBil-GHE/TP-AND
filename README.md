# TP1 - Analyse de données

Cette application Python présente une analyse simple des heures de travail (`HEVR`)
et des notes (`NOTE`) de cinq étudiants. Elle affiche :

- les données utilisées ;
- les moyennes et variances ;
- la covariance et la corrélation de Pearson ;
- les matrices de distances euclidiennes et de Manhattan.

Les résultats sont affichés dans une interface graphique Tkinter et les matrices
de distances sont également imprimées dans le terminal au démarrage.

## Prérequis

- Python 3.9 ou version ultérieure ;
- `pip` ;
- Tkinter, généralement fourni avec Python. Sur Debian/Ubuntu, installez-le si
  nécessaire :

  ```bash
  sudo apt install python3-tk
  ```

## Installation

Depuis le dossier du projet, créez et activez un environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installez ensuite les dépendances :

```bash
python -m pip install --upgrade pip
python -m pip install numpy pandas
```

## Exécution

Avec l'environnement virtuel déjà activé :

```bash
python tp1.py
```

Le script `runTPenv.sh` permet uniquement d'activer l'environnement virtuel
existant :

```bash
./runTPenv.sh
python tp1.py
```

Si l'environnement `.venv` n'existe pas, le script affiche une erreur. Créez-le
au préalable en suivant les instructions d'installation ci-dessus.

## Fichiers principaux

- `tp1.py` : code de l'application et données d'exemple ;
- `runTPenv.sh` : activation de l'environnement virtuel local ;
- `Text File.txt` : ancien mémo de commande.
