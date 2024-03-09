def display_menu():
    print("What city do you want to scrape data from?")
    print("1. Warszawa")
    print("2. Gdańsk")
    print("3. Kraków")
    print("4. Wrocław")
    print("5. Poznań")
    print("6. Elbląg")
    print("7. Łódź")
    print("8. Bydgoszcz")


def get_city_choice():
    city_mapping = {
        '1': 'mazowieckie/warszawa/warszawa/warszawa',
        '2': 'pomorskie/gdansk/gdansk/gdansk',
        '3': 'malopolskie/krakow/krakow/krakow',
        '4': 'dolnoslaskie/wroclaw/wroclaw/wroclaw',
        '5': 'wielkopolskie/poznan/poznan/poznan',
        '6': 'warminsko--mazurskie/elblag/elblag/elblag',
        '7': 'lodzkie/lodz/lodz/lodz',
        '8': 'kujawsko--pomorskie/bydgoszcz/bydgoszcz/bydgoszcz'
    }

    while True:
        choice = input("Enter the number corresponding to the city: ")
        if choice in city_mapping:
            return city_mapping[choice]
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")