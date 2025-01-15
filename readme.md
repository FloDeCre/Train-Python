Exercice : Gestionnaire de commandes
Tu travailles pour une petite boutique en ligne. On te demande de créer un script Python qui aide à gérer les commandes des clients.

Spécifications :
1 - Les clients commandent des articles sous forme de dictionnaires avec :

name : Nom de l'article (chaîne de caractères).
price : Prix unitaire (float).
quantity : Quantité commandée (int).
Exemple :
orders = [
    {"name": "Laptop", "price": 899.99, "quantity": 1},
    {"name": "Mouse", "price": 19.99, "quantity": 2},
    {"name": "Keyboard", "price": 49.99, "quantity": 1},
]
2 - Écris une fonction calculate_total(orders) qui calcule et renvoie le total des commandes.

3 - Ajoute une fonction apply_discount(total, discount) qui applique un pourcentage de réduction au total :

Si le total est supérieur à 1000, applique 10 % de réduction.
Si le total est entre 500 et 1000, applique 5 % de réduction.
Sinon, pas de réduction.

4 - Affiche un récapitulatif de la commande avec :

Les articles commandés (nom, quantité, prix total par article).
Le total avant réduction.
La réduction appliquée (en pourcentage et en valeur).
Le total après réduction.