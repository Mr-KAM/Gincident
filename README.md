# Gincident

<h1> Cahier de charge conception d'une application web de gestion d'incidents et de suivi des actions.</h1>

Une application de gestion des incidents

# **1. Présentation générale du projet**

Ce projet vise à mettre en place une application web sécurisée dédiée à la gestion des incidents et au suivi des actions correctives et préventives pour y remédier.

L’objectif principal de cette solution est de fournir un outil centralisé et accessible permettant :

- La déclaration rapide et facile des incidents qui surviennent dans différentes entreprise par les référents des entreprises.
- Le suivi des incidents signalés, avec une traçabilité complète.
- La gestion structurée des actions correctives et préventives.
- L’amélioration de la communication entre les parties prenantes.


# **2. Description fonctionnelle**

## **2.1 Fonctionnalités principales**

Les fonctionnalités clés de la solution visent à offrir une plateforme sécurisée, intuitive et performante pour la gestion proactive des incidents, le suivi des actions correctives et préventives, ainsi que l’analyse et la visualisation des données critiques en temps réel. Elles sont au nombre de 6 et sont énumérées ci-dessous.
### **2.1.1. Gestion des Niveaux d’Authentification**

- Implémentation d’un système de sécurité robuste basé sur des rôles et permissions.
- Accès sécurisé à l’application avec authentification
- Gestion des profils utilisateurs (administrateurs, utilisateurs standard, etc.).

### **2.1.2. Déclaration d’Incidents**

- Formulaire interactif permettant la saisie des détails d’un incident (type, localisation, description, impact, etc.).
- Possibilité de joindre des fichiers ou des images pour documenter les incidents.

### **2.1.3. Déclenchement d’Actions Correctives et Préventives**

- Création et gestion des actions correctives ou préventives directement liées à un incident.
- Affectation des actions à des responsables avec des échéances définies.
- Notifications automatiques pour alerter les parties concernées des actions en attente ou en retard.

### **2.1.4. Dashboard Interactif**

- Visualisation en temps réel des indicateurs clés (nombre d’incidents ouverts, actions en cours, délais moyens de résolution, etc.).
- Filtrage et personnalisation des données affichées par type d’incident, localisation, ou statut des actions.
- Accès à des graphiques et tableaux pour une analyse rapide et pertinente.

### **2.1.5. Génération de Rapports d’Incidents**

- Génération automatique de rapports détaillés pour un ou plusieurs incidents.
- Formats exportables (PDF et/ou Excel) pour le partage et l’archivage.
- Possibilité d’inclure des statistiques et analyses sur les tendances des incidents.

### **2.1.6. Cartographie Interactive des Incidents et Risques**

- Affichage géolocalisé des incidents sur une carte interactive.
- Indication visuelle des zones à risque ou des lieux ayant enregistré un grand nombre d’incidents.
- Fonctionnalités de zoom, filtres par type d’incident ou gravité, et consultation des détails à partir de la carte.

### **2.2 Rôles et permissions des utilisateurs**

L'application repose sur une structure hiérarchisée des rôles afin de garantir une utilisation sécurisée et adaptée aux responsabilités des utilisateurs. Deux principaux rôles sont définis :

### **2.2.1. Administrateur principal**
    
L'Administrateur Principal dispose de l’ensemble des droits et permissions au sein de l’application.
Il a la capacité de :
        - Créer et gérer les comptes des utilisateurs référents.
        - Déclencher et attribuer des actions correctives ou préventives.
        - Générer des rapports détaillés sur les incidents et les actions entreprises.
        - Envoyer des notifications ciblées aux utilisateurs référents pour les informer des incidents, actions en cours, ou rappels de délais.
Ce rôle garantit une supervision globale et un contrôle total sur les processus et les données.
### **2.2.2. Référents Utilisateurs**
    
Les Référents Utilisateurs sont les points focaux au sein des différentes entités de l’entreprise. Il on la responsabilité de déclarer les incidents.
Ils ont pour responsabilités principales :
        - Déclarer les incidents en fournissant les informations pertinentes.
        - Collaborer sur les actions correctives ou préventives assignées.
        - Consulter les notifications et les informations partagées par l’Administrateur Principal.

Leur rôle est essentiel pour garantir la remontée rapide et précise des incidents depuis les différentes unités opérationnelles.

### **2.3 Interface utilisateur (UI/UX)**


L'interfaces utilisateurs comprendra les fenêtres suivantes :

- pages d'authentification
- pages d'accueil
- gestions des incidents
- gestions des actions
- tableaux de bord
- cartographie des incidents

# **3. Contraintes techniques**

## **3.1 Technologies utilisées**

### **3.1.1.  Langages de programmation**

#### **- HTML (HyperText Markup Language)**

**Rôle :**

- HTML est le langage de base utilisé pour structurer le contenu des pages web.
- Il définit la structure des éléments tels que les titres, paragraphes, formulaires de saisie, tableaux, et autres composants visibles de l'application.

**Pourquoi l’utiliser :**

- Il est essentiel pour créer une interface utilisateur accessible et bien organisée.
- Compatible avec tous les navigateurs web.
- Fournit un cadre standard pour intégrer d'autres technologies comme CSS et JavaScript.

#### **- CSS (Cascading Style Sheets)**

**Rôle :**

- CSS est utilisé pour styliser et rendre l'application visuellement attrayante.
- Il permet de contrôler la mise en page, les couleurs, les polices, les marges, et le design global de l'application.

**Pourquoi l’utiliser :**

- Il garantit une interface utilisateur esthétique et conviviale, adaptée aux différents appareils (responsive design).
- Permet de séparer la présentation visuelle du contenu HTML, rendant le code plus propre et plus facile à maintenir.
- Prend en charge les animations pour améliorer l'expérience utilisateur.

#### **- JavaScript**

**Rôle :**

- JavaScript est utilisé pour rendre l'application interactive et dynamique.
- Il gère les événements utilisateur, tels que les clics de bouton, les validations de formulaire, ou les mises à jour en temps réel des données affichées sur l'écran.

**Pourquoi l’utiliser :**

- Permet d'ajouter des fonctionnalités interactives comme les tableaux de bord, les graphiques dynamiques, et les cartes interactives pour la cartographie des incidents.
- Facilite la communication en temps réel avec le serveur grâce à des technologies comme AJAX.
- Les frameworks comme React ou Vue.js (basés sur JavaScript) peuvent être utilisés pour construire des interfaces utilisateur modernes et réactives.


#### **- Python**

**Rôle :**

- Python est utilisé côté serveur pour gérer la logique métier, les interactions avec la base de données, et les fonctionnalités critiques de l'application.
- Il est également utilisé pour les tâches d’analyse des données et la génération de rapports.

**Pourquoi l’utiliser :**

- Python offre une vaste gamme de frameworks comme Django et Flask, qui simplifient le développement backend grâce à des outils robustes pour gérer la sécurité, les autorisations, et la gestion des utilisateurs.
- Il est efficace pour manipuler des données complexes, générer des rapports d’incidents automatisés, et exécuter des algorithmes liés à l’analyse des risques.
- Sa syntaxe simple et lisible accélère le développement, le rendant parfait pour les projets nécessitant une collaboration.


#### **Résumé**

| **Langage**    | **Rôle**                                                  | **Usage**                                                                                                               |
| -------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **HTML**       | Structure des pages web                                   | Définit la structure des éléments comme les formulaires, tableaux, et composants visibles de l'application.             |
| **CSS**        | Design et esthétique                                      | Gère les styles (couleurs, polices, marges) et rend l'application responsive et visuellement attrayante.                |
| **JavaScript** | Interactivité et dynamisme côté client                    | Ajoute des fonctionnalités interactives (cartes, graphiques, validation de formulaire) et actualisations dynamiques.    |
| **Python**     | Gestion backend, logique métier et traitement des données | Gère la logique serveur, les interactions avec la base de données, l’analyse des données, et la génération de rapports. |

### 3.1.2. Base de données 

Nous utiliseront comme base de données une base de données MySQL. Cette base de données contiendra les tables suivantes : 

#### **1. Table : `referents`**

### Description :

Les référents sont responsables de la gestion des utilisateurs et des groupes dans l'application.

### Attributs :

- `id` (PK) : Identifiant unique du référent.
- `nom` : Nom du référent.
- `prenom` : Prénom du référent.
- `matricule` : Matricule unique.
- `structure` : Structure à laquelle appartient le référent.
- `email` : Adresse e-mail du référent.
- `telephone` : Numéro de téléphone.
- `mot_de_passe` : Mot de passe crypté.
- `date_naissance` : Date de naissance.
- `adresse` : Adresse physique.


#### **2. Table : `entreprises`**

**Description :**

Cette table regroupe les informations relatives aux entreprises utilisant l'application.

**Attributs :**

- `id` (PK) : Identifiant unique de l’entreprise.
- `nom` : Nom de l’entreprise.
- `adresse` : Adresse complète de l’entreprise.
- `telephone` : Numéro de téléphone de l’entreprise.
- `email` : Adresse e-mail.
- `site_web` : URL du site web.
- `pays` : Pays (liste déroulante).
- `siege_ville` : Ville du siège social.
- `date_creation` : Date de création de l’entreprise.
- `zone_activite` : Zone d’activités (liste prédéfinie).
- `longitude_siege` : Longitude du siège.
- `latitude_siege` : Latitude du siège.
- `logo` : Chemin ou lien vers le logo de l’entreprise.


#### **3. Table : `zones`**

**Description :**

Les zones sont des localisations spécifiques utilisées pour la gestion des incidents.

**Attributs :**

- `id_zone` (PK) : Identifiant unique de la zone.
- `nom` : Nom de la zone.
- `longitude_zone` : Longitude de la zone.
- `latitude_zone` : Latitude de la zone.


#### **4. Table : `incidents`**

**Description :**

Cette table regroupe toutes les informations relatives aux incidents signalés.

**Attributs :**

- `id` (PK) : Identifiant unique de l’incident.
- `date_incident` : Date de l’incident.
- `heure_incident` : Heure de l’incident.
- `type_incident` : Type d’incident (liste prédéfinie).
- `localisation` : Secteur ou zone où l’incident s’est produit.
- `niveau_risque` : Niveau de risque (échelle de 1 à 10).
- `identifie_par` : Nom de la personne ayant identifié l’incident.
- `rapporte_par` : Nom de la personne ayant rapporté l’incident.
- `tiers_implique_nom` : Nom des tiers impliqués.
- `tiers_implique_nationalite` : Nationalité des tiers impliqués.
- `tiers_implique_telephone` : Téléphone des tiers impliqués.
- `temoin_nom` : Nom du témoin.
- `temoin_nationalite` : Nationalité du témoin.
- `temoin_telephone` : Téléphone du témoin.
- `resume` : Résumé de l’incident.
- `observations` : Observations liées à l’incident.
- `causes` : Causes identifiées de l’incident.
- `actions` : Actions entreprises en réponse à l’incident.
- `media` : Lien ou chemin vers les fichiers multimédia associés.


#### **5. Table : `actions`**

**Description :**

Cette table décrit les actions correctives ou préventives associées aux incidents.

**Attributs :**

- `id` (PK) : Identifiant unique de l’action.
- `intitule` : Intitulé ou description de l’action.
- `responsable_referent` : Identifiant du référent responsable (FK vers `referents`).
- `responsable_terrain` : Identifiant de la personne sur le terrain.
- `date_creation` : Date de création de l’action.
- `date_debut` : Date de début de la mise en œuvre.
- `date_limite` : Date limite pour la réalisation.
- `etat` : État de l’action (`Neutre`, `Urgent`).


## **3.2 Hébergement et infrastructure**

Un hébergeur externe sera utilisé. Il s'agira de PythonAnywhere ou une autre solution dans ce sens.
## **3.3 Sécurité**

- Exigences en matière de sécurité (authentification, protection des données, conformité RGPD).

---

# **4. Planning et jalons**

## **4.1 Étapes de développement**

- [ ] Analyse des besoins               | Vendredi 6
- [ ] Design et prototypage            |  Mercredi 11
- [ ] Développement                       |  Mercredi 18
- [ ] Tests et corrections.               | Mercredi 25
- [ ] Déploiement.                           | Mardi 31 

| **Tâche**             | **Date**    | **Statut** |
| --------------------- | ----------- | ---------- |
| Analyse des besoins   | Vendredi 6  | [ ]        |
| Design et prototypage | Mercredi 11 | [ ]        |
| Développement         | Mercredi 18 | [ ]        |
| Tests et corrections  | Mercredi 25 | [ ]        |
| Déploiement           | Mardi 31    | [ ]        |

## **4.2 Livrables attendus**

- [ ] Le cahier de charge de l'application
- [ ] Une application web fonctionnelle accessibles par les différentes parties prenantes avec leurs niveaux d'administrations respectifs. 
- [ ] Le code source de l'application

## **4.3 Délais**

Le projet s'étends sur un délai maximum de  25 jours a compté du 05/12/2024.

La date de livraison est donc prévu pour le 31 décembre 2024.