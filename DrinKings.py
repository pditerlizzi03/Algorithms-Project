def main():
    # PROFILE CREATION

    print('Welcome to DrinKings!')

    print('\nLets get started with creating your profile')
    name = input('Enter your first and last name ')
    email = input('Enter your email address ')
    password = input('Enter your password ')


main()


def alcohol():
    # DRINK SELECTION ALGORITHM

    Drinks = {'Whiskey': 0.47, 'Rum': 0.375, 'Vodka': 0.40, 'Tequila': 0.40, 'Gin': 0.40, 'Orujo': 0.375,
              'Coñac': 0.40, 'Fernet': 0.43, 'Soju': 0.35, 'Ginjinha': 0.18}
    drink_vol = 100

    Shots = {'Jaggermeister': 0.35, 'Limoncello': 0.30, 'Tequila': 0.40, 'Grand Marnier': 0.40, 'Brandy': 0.45,
             'Schnapps': 0.23, 'Aguardiente': 0.30, 'Fireball': 0.33, 'Absenta': 0.65, 'Pisco': 0.40}
    shots_vol = 40

    Beers = {'Corona': 0.04, 'Heineken': 0.05, 'Mahou': 0.055, 'Budweiser': 0.05, 'Weidmann': 0.12, 'La Salve': 0.062,
             'Estrella Galicia': 0.055, 'Amstel': 0.05, 'Stella Artois': 0.05, 'Pilsen': 0.044}
    beers_vol = 355

    Coctails = {'Moscow Mule': 0.11, 'Margarita': 0.19, 'Mojito': 0.13, 'Blue Lagoon': 0.20, 'Paloma': 0.12,
                'Dry Martini': 0.26, 'Piña Colada': 0.13}
    coctails_vol = 200

    Champagnes = {'GH Mumm': 0.125, 'Moet&Chandon': 0.12, 'Bollinger': 0.12, 'Veuve Cliquot': 0.12, 'Lanson': 0.125,
                  'Nicolas Feuillate': 0.12, 'Laurent-Perrier': 0.12, 'Don Perignon': 0.13, 'Pommery': 0.125,
                  'Piper-Heidsieck': 0.12}
    champagne_vol = 180

    Wines = {'Cabernet Sauvignon': 0.125, 'Ribera del Duero': 0.11, 'Pinot Noir': 0.11, 'Albariño': 0.12,
             'Malbec': 0.135,
             'Rioja': 0.105, 'Tempranillo': 0.143, 'Pago de los Capellanes': 0.15, 'Marqués de Murrieta': 0.125,
             'Izadi Larrosa Rosé': 0.14}
    wine_vol = 340

    drink_list = []

    print('\nPlease remember that to drink safely choose only three alcoholic beverages at max')
    print('\nThese are all the drinks to choose from:')
    print(Drinks.keys())
    Drink_Election = input('What type of drink do you want to have? (<Enter> if you want no drinks) ')
    while Drink_Election != '':
        percentage = Drinks.get(Drink_Election) * 100
        drink_units = (percentage * drink_vol) / 1000
        print((Drink_Election, drink_units))
        drink_list.append((Drink_Election, drink_units))
        Drink_Election = input('What other drink type do you want to have? (<Enter> if you want no  more drinks) ')

    print('\nThese are all the shots to choose from:')
    print(Shots.keys())
    Shots_Election = input('What type of shot do you want to have? (<Enter> if you want no shots) ')
    while Shots_Election != '':
        percentage = Shots.get(Shots_Election) * 100
        shot_units = (percentage * shots_vol) / 1000
        print((Shots_Election, shot_units))
        drink_list.append((Shots_Election, shot_units))
        Shots_Election = input('What other shot type do you want to have? (<Enter> if you want no  more shots) ')

    print('\nThese are all the beers to choose from:')
    print(Beers.keys())
    Beer_Election = input('What type of beer do you want to have? (<Enter> if you want no beers) ')
    while Beer_Election != '':
        percentage = Beers.get(Beer_Election) * 100
        beer_units = (percentage * beers_vol) / 1000
        print((Beer_Election, beer_units))
        drink_list.append((Beer_Election, beer_units))
        Beer_Election = input('What other beer type do you want to have? (<Enter> if you want no  more beers) ')

    print('\nThese are all the wines to choose from:')
    print(Wines.keys())
    Wine_Election = input('What type of wine do you want to have? (<Enter> if you want no wine) ')
    while Wine_Election != '':
        percentage = Wines.get(Wine_Election) * 100
        wine_units = (percentage * wine_vol) / 1000
        print((Wine_Election, wine_units))
        drink_list.append((Wine_Election, wine_units))
        Wine_Election = input('What other wine type do you want to have? (<Enter> if you want no  more wine) ')

    print('\nThese are all the champagnes to choose from:')
    print(Champagnes.keys())
    Champagne_Election = input('What type of champagne do you want to have? (<Enter> if you want no champagne) ')
    while Champagne_Election != '':
        percentage = Champagnes.get(Champagne_Election) * 100
        champagne_units = (percentage * champagne_vol) / 1000
        print((Champagne_Election, champagne_units))
        drink_list.append((Champagne_Election, champagne_units))
        Champagne_Election = input(
            'What other champagne type do you want to have? (<Enter> if you want no more champagne) ')

    print('\nThese are all the coctails to choose from:')
    print(Coctails.keys())
    Coctail_Election = input('What type of coctail do you want to have? (<Enter> if you want no coctails) ')
    while Coctail_Election != '':
        percentage = Coctails.get(Coctail_Election) * 100
        coctail_units = (percentage * coctails_vol) / 1000
        print((Coctail_Election, coctail_units))
        drink_list.append((Coctail_Election, coctail_units))
        Coctail_Election = input('What other coctail type do you want to have? (<Enter> if you want no more coctails) ')

    if len(drink_list) > 3:
        print(
            '\nThis is not very safe, you should not be mixing too many alcohols, please try to only chose 3 alcoholic drinks at max')
        return alcohol()

    print()
    print(drink_list)
    return drink_list


drink_list = alcohol()


def convert(list):
    dict = {}
    for tuple in list:
        dict[tuple[0]] = tuple[1]
    return dict


selected_drinks = convert(drink_list)


def tracker(hashtable):
    print('\nWe need some basic information about you before we can get completely started')
    age = eval(input('What is your age? '))
    if age < 18:
        print('\nYou should not be drinking at this age, come back when you are 18 years old or older.')
    else:
        weight = eval(input('What is your weight (kg)? '))
        calories = eval(input('How many calories did you consume today? '))
        print('\nPerfect! You are ready to go!')
        print('Party safely and get ready to have the best nights of your life!')
        consumption_units = 0.1335 * (weight) + 0.003 * (calories) + 1.835
        print()
        print('You have', consumption_units, 'alcohol units to consume!')
        print('\nPlease remember to distribute your drinks during the night and not drink to quickly')
        print('Also note ot is key to drink water in between drinks')

        print(
            '\nThe night has just begun, type out the drink name once you consume it and you will get those units deducted from your total.')
        print()
        consumption = input('What drink from the previously selected are you going to have?')
        while consumption_units > 0:
            consumption_units = consumption_units - hashtable.get(consumption)
            if consumption_units > 0:
                print('\nYou have', consumption_units, 'alcohol units left to consume; Drink responsibly :)')
                consumption = input('Do you want another drink? If so which one of the previously chosen?')
            else:
                break


tracker(selected_drinks)

print('\nThis is your reminder to stop drinking for the night, do not take that last drink')
print('Thank you for trusting drinkings!')




