# **Telegram Template**

Telegram Template  est un modèle conçu pour être adapté à différentes missions spécialisées. Utilisez ce modèle comme point de départ pour créer des assistants personnalisés selon les besoins spécifiques de chaque domaine. Chaque assistant spécialisé peut se présenter en utilisant le gras Markdown lors de son introduction.

### Missions Principale

1. **Recommandations Personnalisées :** L'assistant a la capacité de recommander des éléments spécifiques en fonction de la mission donée.

2. **Fourniture d'Informations :** Il peut fournir des détails pertinents sur des sujets spécifiques, y compris des données telles que les dates, les chiffres, et les faits.

3. **Conseils et Guidage :** L'assistant est là pour guider les utilisateurs en leur fournissant des conseils personnalisés dans un domaine particulier.

4. **Exploration et Identification :** Il peut identifier des éléments spécifiques en fonction de critères donnés, facilitant ainsi l'exploration et la découverte.

5. **Réponses aux Questions :** L'assistant répond aux questions courantes et fournit des informations utiles dans son domaine d'expertise.

### Personnalisation :

- Ajoutez des sections spécifiques pour chaque assistant, détaillant les compétences uniques et les connaissances nécessaires.
- Personnalisez les exemples et les missions en fonction du domaine d'expertise de chaque assistant.

Utilisez ce modèle comme point de départ pour créer des assistants spécialisés pour différentes tâches et domaines. Chaque assistant peut être adapté en fonction de ses missions et de son contexte d'utilisation.

## **Installation**
### Prérequis
- [Docker](https://docs.docker.com/get-docker/)

## Running the app
### Windows
```bash
docker build -t telegram-template . ; docker run --rm telegram-template
```
### Mac
```bash
docker build -t telegram-template . && docker run --rm telegram-template
```

si réseau docker local pour booter smart :
```bash
docker build -t telegram-template . && docker run --rm --network smart_bridge telegram-template
```