# City Functions.

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Function calls
print(city_country("santiago", "chile", 5000000, "Spanish"))
print(city_country("paris", "france", 2148000))
print(city_country("tokyo", "japan", 13960000))
