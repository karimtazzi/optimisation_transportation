
# Problème de Transport - Optimisation Linéaire

## Description du Problème

Le **problème de transport** est un problème d'optimisation où l'objectif est de minimiser le coût total du transport de marchandises entre plusieurs entrepôts et plusieurs destinations. Le modèle prend en compte les coûts unitaires de transport, les capacités des entrepôts et les demandes des destinations.

Le problème peut être formulé comme suit :

- Il y a un certain nombre d'entreprises ou d'entrepôts qui peuvent fournir des marchandises.
- Il existe plusieurs destinations (ou clients) qui demandent des quantités de marchandises.
- Chaque entrepôt a une capacité maximale d'expédition.
- Chaque destination a une demande spécifique qui doit être satisfaite.
- Le but est de déterminer combien de marchandises doivent être envoyées de chaque entrepôt à chaque destination de manière à minimiser le coût total du transport, tout en respectant les contraintes de capacité des entrepôts et de demande des destinations.

## Méthodologie de Résolution

### 1. **Initialisation des Données**

- **coûts** : Une matrice représentant les coûts unitaires de transport entre chaque entrepôt et chaque destination.
  - `costs[i][j]` représente le coût de transport de l'entrepôt \(i\) vers la destination \(j\).
  
- **capacités** : Une liste des capacités maximales d'expédition pour chaque entrepôt.
  - `capacities[i]` représente la capacité de l'entrepôt \(i\).

- **demandes** : Une liste des demandes minimales pour chaque destination.
  - `demands[j]` représente la demande de la destination \(j\).

### 2. **Définition du Modèle**

Le problème est formulé comme un **problème d'optimisation linéaire** où l'on cherche à minimiser le coût total de transport. Le modèle est défini à l'aide de la bibliothèque **PuLP** pour Python, qui permet de formuler et résoudre des problèmes d'optimisation linéaire.

#### Variables de Décision
- \( 	ext{transport\_qty}_{(i, j)} \) représente la quantité de marchandises envoyée de l'entrepôt \(i\) vers la destination \(j\).

#### Fonction Objectif
L'objectif est de minimiser le coût total du transport, qui est donné par :
\[
	ext{Minimiser} \, \sum_{i, j} 	ext{coûts}[i][j] 	imes 	ext{transport\_qty}_{(i, j)}
\]

#### Contraintes
1. **Contraintes de capacité** :
   \[
   \sum_{j} 	ext{transport\_qty}_{(i, j)} \leq 	ext{capacités}[i]
   \]
   Cela garantit que la quantité totale expédiée depuis chaque entrepôt ne dépasse pas sa capacité.

2. **Contraintes de demande** :
   \[
   \sum_{i} 	ext{transport\_qty}_{(i, j)} \geq 	ext{demandes}[j]
   \]
   Cela assure que chaque destination reçoit au moins la quantité demandée.

### 3. **Résolution du Problème**

Le problème est résolu en utilisant l'algorithme d'optimisation linéaire de **PuLP**, qui détermine les valeurs optimales des variables de décision \( 	ext{transport\_qty}_{(i, j)} \) qui minimisent le coût tout en respectant les contraintes.

### 4. **Extraction des Résultats**

Une fois le problème résolu, les résultats incluent :
- **Coût total du transport**, qui est la valeur optimale de la fonction objectif.
- **Quantités optimales de transport** entre chaque entrepôt et chaque destination.

Le programme génère un dictionnaire des quantités optimales à transporter et affiche également le coût total du transport.

## Exemple d'Exécution

### Données d'entrée :
```python
costs = [
    [15, 160, 154, 245, 130, 125, 215],
    [160, 12, 315, 410, 290, 427, 375],
    [100, 260, 56, 190, 58, 204, 160]
]
capacities = [3980, 1785, 4856]
demands = [1168, 1560, 1439, 986, 1658, 2035, 1159]
```

### Résultats possibles :
```
Total Transportation Cost: 12345.67
Optimal Transport Qty from Warehouse 1 to Destination 1: 500.00
Optimal Transport Qty from Warehouse 1 to Destination 2: 600.00
...
```

Les résultats affichent le coût total du transport et les quantités optimales à envoyer de chaque entrepôt vers chaque destination.

## Installation et Exécution

### Prérequis
- Python 3.x
- La bibliothèque **PuLP** doit être installée. Vous pouvez l'installer avec la commande suivante :

```bash
pip install pulp
```

### Exécution
Vous pouvez exécuter le programme directement dans un script Python. Le code résout le problème en utilisant les données d'entrée fournies et affiche les résultats optimaux.

