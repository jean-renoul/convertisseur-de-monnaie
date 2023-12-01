from forex_python.converter import CurrencyRates

historique = []
monnaies_favorites = []
liste_monnaie = ["USD", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD",
                 "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "EUR", "NOK", "RUB", "INR", "MXN", "CZK",
                 "BRL", "PLN", "PHP", "ZAR"]


monnaie_ajoutee = "ABC"
monnaie_ajoutee_taux = {"USD": 1.5, "EUR": 1.2, "IDR": 200}

def convertisseur():
    print("monnaies favorites :" , monnaies_favorites)

    devise_base = input("Saisissez la monnaie à convertir : ")
    if devise_base not in monnaies_favorites:
        monnaies_favorites.append(devise_base)
    
    if devise_base not in liste_monnaie and devise_base != monnaie_ajoutee:
        print("Devise incorrecte")
        monnaies_favorites.pop()
        convertisseur()

    devise_destination = input("Saisissez la monnaie souhaitée : ")
    if devise_destination not in monnaies_favorites:
        monnaies_favorites.append(devise_destination)
    
    if devise_destination not in liste_monnaie and devise_destination != monnaie_ajoutee:
        print("Devise incorrecte")
        monnaies_favorites.pop()
        convertisseur()

    valeur = int(input("Saisissez une valeur entière à convertir : "))

    c = CurrencyRates()

    if devise_base == monnaie_ajoutee:
        resultat = valeur * monnaie_ajoutee_taux[devise_destination]
    elif devise_destination == monnaie_ajoutee:
        resultat = valeur / monnaie_ajoutee_taux[devise_base]
    else:
        resultat = c.get_rate(devise_base, devise_destination) * valeur

    print(resultat)

    historique_input = input("Voulez-vous sauvegarder cette conversion ? ")    
    if historique_input == "oui":
        historique.append(devise_base + "-->" + devise_destination + " x " + str(valeur) + " = " + str(resultat))

    afficher_historique = input("Voulez-vous afficher l'historique ? ")    
    if afficher_historique == "oui":
        print(historique)

    supprimer_historique = input("Voulez-vous supprimer l'historique ? ")    
    if supprimer_historique == "oui":
        historique.clear()

    convertisseur()

convertisseur()