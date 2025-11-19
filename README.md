# Bienvenue dans ce projet d'IA

Installation : 

    python -m venv .venv


Activation :

Windows (PowerShell) :

    .\.venv\Scripts\Activate.ps1

Windows (CMD) :

    .\.venv\Scripts\activate.bat

macOS / Linux :

    source .venv/bin/activate


Installation des dépendances : 

    pip install -r requirements.txt


# Le modèle d'IA

Nous avons ici un réseau de neurones (NN) avec :
2 couches "denses"
1 couche de prédiction

# Architecture du projet

    .
    ├── data/
    │   ├── df_new.csv
    │   └── df_old.csv
    ├── models/
    │   ├── models.py
    │   ├── model_2024_08.pkl
    │   └── preprocessor.pkl
    ├── modules/
    │   ├── evaluate.py
    │   ├── preprocess.py
    │   └── print_draw.py
    ├── .gitignore
    ├── README.md
    ├── main.py
    └── requirements.txt


data/ 

C'est là que sont stockées les données.

    df_new.csv : Les données fraîches du jour, prêtes à être dévorées par notre IA.
    df_old.csv : Les anciennes données ayant servis à l'apprentissage initial du modèle

models/ 

C'est là que sont stockés les modèles

    models.py : C'est ici que l'on définit l'architecture de notre NN.
    model_2024_08.pkl : Une version sauvegardée de notre modèle. 
    preprocessor.pkl : le preparateur de données

modules/ 

C'est là que le code python se découpe en modules ayant chaque une tâche définie

    evaluate.py : Module d'évaluation du modèle.
    preprocess.py : Module de préparation des données
    print_draw.py : Module d'affichage des résultats

# Travaux demandés – Réentraînement du modèle et monitoring

## Contexte du brief

Ce projet s'inscrit dans le cadre de FastIA. Le modèle initial mis en production a perdu en performance car les données réelles ont évolué. L'objectif est de réentraîner ce modèle avec de nouvelles données et de mettre en place un monitoring de ses performances.

## Pipeline de réentraînement

Script `train.py` (lance le réentraînement et logge les métriques):
1. Chargement des données (`df_old`, `df_new`).
2. Prétraitement avec le préprocesseur fournis (`models/preprocessor.pkl`).
3. Isolation des données d'entraînement et de test.
4. Chargement de l'ancien modèle depuis MLflow (sauvegardée lors d'une expérience précédente).
5. Expérience précédente : évaluation de l'ancien modèle sur les nouvelles données.
6. Réentraînement du modèle sur le nouveau jeu de données.
7. Test des nouvelles données sur le nouveau modèle.
8. Logging des métriques et du modèle dans MLflow.

## Métriques suivies

Les métriques suivantes sont suivies :

- **MSE** (Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **R²** (Coefficient de détermination)

Ces métriques sont loggées dans MLflow pour chaque run.

## Résultats

Résumé des performances (exemple, à adapter avec tes chiffres) :

| Run                | Description                                                    | MSE      | MAE    | R²   |
|--------------------|---------------------------------------------------------------:|---------:|-------:|-----:|
| receptive-roo-789  | Evaluation de l'ancien modèle avec les nouvelles données.      | 29218372 | 4104.9 | 0.74 |
| likeable-newt-318  | Re-entraînement de l'ancien modèle avec les nouvelles données. | 13547699 | 2414.0 | 0.87 |

Le modèle réentraîné présente une amélioration des performances : baisse du MSE et du MAE et augmentation du R².

## Monitoring et MLflow

Les expériences sont gérées avec MLflow :

- Comparaison des runs dans l'UI MLflow (`python3 -m mlflow ui`).
- Sauvegarde des modèles (`mlflow.sklearn.log_model`).

Des captures d’écran de l’interface MLflow sont fournis en support.

## Remarques

Lors de l'expérience de réentraînement de l'ancien modèle avec les anciennes données, les performances se sont améliorées.
Cependant, ceci est dû au fait que les données de tests sont choisies aléatoirement par la fonction split.
Des données du jeu de tests sont donc présentes dans les données d'entraînement, ce qui fausse la metrique de performance.

