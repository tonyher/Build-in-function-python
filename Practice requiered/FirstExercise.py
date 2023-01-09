
def getCountries():
    countries = []

    for i in range(5):
        country= input("Introduce any country: ")
        countries.append(country)
    
    countries = set(countries)
    newList= sorted(countries)
    print(newList)

getCountries()