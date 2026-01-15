# automation-project-saucedemo
Projet d'automatisation de tests pour Saucedemo.com

Projet CORP QA - Automatisation de Tests Détaillé pour Saucedemo.com

Description du Projet

Ce projet pratique vise à mettre en œuvre un cadre d'automatisation de tests robuste pour l'application web Saucedemo.com. L'objectif est de pratiquer diverses technologies et méthodes de travail (DevOps, SCRUM, Intégration Continue) en couvrant les fonctionnalités principales de l'application via cinq tests automatisés distincts.

TechnologieLangageNombre de TestsPlaywrightJavaScript2SeleniumPython2Robot FrameworkSelenium Library1

Le projet utilise également Git pour le versionnement, JIRA XRAY pour la gestion des cas de test et des résultats, et Jenkins pour l'intégration et l'exécution continues.

1. Prérequis d'Installation

Pour exécuter les tests localement, vous devez disposer des éléments suivants :

1. Node.js et npm (pour Playwright).

2. Python 3.x (pour Selenium et Robot Framework).

3. Git.

1.1 Configuration des Dépendances

A. Dépendances Python (Selenium et Robot Framework)

Créez et activez un environnement virtuel, puis installez les dépendances listées dans requirements.txt :

pip install -r requirements.txt

(Le fichier requirements.txt doit contenir au minimum : selenium==4.y.z, robotframework==6.y.z, robotframework-seleniumlibrary==6.y.z).

B. Dépendances JavaScript (Playwright)

Accédez au répertoire playwright_tests/ et installez les dépendances Node.js listées dans package.json :

npm install
npx playwright install

2. Structure du Projet

Le projet est organisé autour des différentes technologies d'automatisation :

.
├── jenkins/                     # Fichiers de configuration Jenkins (Jenkinsfile)
├── playwright_tests/            # Tests Playwright en JavaScript (CCS-1, CCS-2)
├── robot_tests/                 # Test Robot Framework (CCS-5)
├── selenium_tests/              # Tests Selenium en Python (CCS-3, CCS-4)
├── reports/                     # Rapports de test générés (HTML, XML, JSON)
├── requirements.txt             # Dépendances Python
├── package.json                 # Dépendances JavaScript
└── README.md                    # Documentation du projet

3. Instructions d'Exécution des Tests

Vous pouvez exécuter chaque suite de tests indépendamment en local, ou via le pipeline Jenkins configuré.

3.1 Exécution Locale

TechnologieCommande d'ExécutionDescriptionPlaywrightnpx playwright testExécute les deux tests JavaScript (filtrage et paiement).Selenium Pythonpython -m unittest discover selenium_testsExécute les deux tests Python (erreurs de connexion et vérification produits).Robot Frameworkrobot robot_tests/votre_test.robotExécute le test de navigation du menu burger.

Note : Les tests Playwright sont configurés pour s'exécuter en mode headless. Le rapport HTML peut être visualisé avec npx playwright show-report.

3.2 Exécution via Jenkins (CI/CD)

Le pipeline Jenkins est défini dans le fichier Jenkinsfile, qui orchestre les étapes suivantes :

1. Checkout du code source.

2. Installation des dépendances (Python et Node.js).

3. Exécution des 5 tests (Robot Framework, Playwright, Selenium Python).

4. Publication des rapports HTML.

Pour lancer la suite complète :

1. Assurez-vous que Jenkins est installé localement et que les plugins nécessaires (Pipeline, Robot Framework) sont configurés.

2. Créer un nouveau Pipeline Item pointant vers le Jenkinsfile dans le dépôt Git.

3. Cliquer sur Build Now.

4. Cas de Test Implémentés

Les 5 tests automatisés correspondent aux cas de test JIRA XRAY suivants :

XRAY IDTestTechnologieObjectifCCS-1Filtrage des produitsPlaywrightVérification du tri (A-Z, prix croissant/décroissant).CCS-2Processus de paiementPlaywrightFlux complet d'achat et vérification de la confirmation.CCS-3Gestion des erreursSelenium PythonValidation des messages d'erreur de connexion.CCS-4Vérification des produitsSelenium PythonConfirmation de la présence et des détails des 6 produits.CCS-5Menu BurgerRobot FrameworkTest de toutes les options du menu latéral (Logout, About, Reset).

5. Intégration et Reporting

JIRA XRAY Dashboard

Les résultats des 5 tests sont intégrés et visualisés dans le projet JIRA XRAY (CORP-CSF-SAUCEDEMO-TEST).

Le dashboard JIRA XRAY inclut les widgets suivants pour une vue globale :

- Résumé des tests.

- Progression des tests.

- Historique d'exécution.

- Répartition par technologie.

Utilisateurs de Test

L'application cible utilise les identifiants suivants :

- Utilisateur standard : standard_user / secret_sauce

- Utilisateur avec problème : problem_user / secret_sauce

- Utilisateur verrouillé : locked_out_user / secret_sauce