from forex_python.converter import CurrencyRates

historique = []

monnaies_favorites = []

# Liste des monnaies autorisées pour la conversion
liste_monnaie = ["USD", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD",
                 "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "EUR", "NOK", "RUB", "INR", "MXN", "CZK",
                 "BRL", "PLN", "PHP", "ZAR"]

# Monnaie hypothétique ajoutée avec des taux définis pour certaines monnaies
monnaie_ajoutee = "ABC"
monnaie_ajoutee_taux = {"USD": 1.5, "EUR": 1.2, "IDR": 200}

# Fonction de conversion
def convertisseur():
    print("Monnaies favorites :", monnaies_favorites)

    # Saisit la monnaie de base et l'ajoute dans les monnaies favorites
    devise_base = input("Saisissez la monnaie à convertir : ")
    if devise_base not in monnaies_favorites:
        monnaies_favorites.append(devise_base)

    # Vérifie la validité de la monnaie de base et la retire des monnaies favorites si invalide
    if devise_base not in liste_monnaie and devise_base != monnaie_ajoutee:
        print("Devise incorrecte")
        monnaies_favorites.pop()
        convertisseur()

    # Saisit la monnaie de destination
    devise_destination = input("Saisissez la monnaie souhaitée : ")
    if devise_destination not in monnaies_favorites:
        monnaies_favorites.append(devise_destination)

    # Vérifie la validité de la monnaie de destination
    if devise_destination not in liste_monnaie and devise_destination != monnaie_ajoutee:
        print("Devise incorrecte")
        monnaies_favorites.pop()
        convertisseur()

    # Saisit la valeur à convertir, relance l'input si le nombre est invalide
    while True:
        try:
            valeur = int(input("Saisissez une valeur entière à convertir : "))
            break
        except:
            print ("Veuillez entre un nombre entier")

    c = CurrencyRates()

    # Effectue la conversion en utilisant la monnaie hypothétique si nécessaire
    if devise_base == monnaie_ajoutee:
        resultat = valeur * monnaie_ajoutee_taux[devise_destination]
    elif devise_destination == monnaie_ajoutee:
        resultat = valeur / monnaie_ajoutee_taux[devise_base]
    else:
        resultat = c.get_rate(devise_base, devise_destination) * valeur

    # Affiche le résultat de la conversion
    print(resultat)

    # Demande à l'utilisateur si il veut sauvegarder cette conversion dans l'historique
    historique_input = input("Voulez-vous sauvegarder cette conversion ? (oui/non) ")    
    if historique_input == "oui":
        historique.append(devise_base + "-->" + devise_destination + " x " + str(valeur) + " = " + str(resultat))

    # Demande à l'utilisateur si il veut afficher l'historique
    afficher_historique = input("Voulez-vous afficher l'historique ? (oui/non) ")    
    if afficher_historique == "oui":
        print(historique)

    # Demande à l'utilisateur si il veut supprimer l'historique
    supprimer_historique = input("Voulez-vous supprimer l'historique ? (oui/non) ")    
    if supprimer_historique == "oui":
        historique.clear()

    # Rappele la fonction pour effectuer d'autres conversions
    convertisseur()

# Appele la fonction de conversion pour démarrer le programme
convertisseur()