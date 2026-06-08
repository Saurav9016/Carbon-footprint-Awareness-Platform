def calculate_carbon(car_km, electricity_kwh, flights, diet):

    transport = car_km * 0.21
    electricity = electricity_kwh * 0.42
    air = flights * 90

    diet_factor = {
        "vegan": 2,
        "vegetarian": 4,
        "mixed": 6,
        "nonveg": 8
    }

    food = diet_factor.get(diet, 6)

    total = transport + electricity + air + food

    return round(total, 2)