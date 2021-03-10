countries = input().split(", ")
capitals = input().split(", ")
countries_capitals_dict = {pair[0]: pair[1] for pair in zip(countries, capitals)}
print('\n'.join(f"{country} -> {capital}" for country, capital in countries_capitals_dict.items()))