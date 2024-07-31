travel_log= [
    {
        "countries": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    }
    ,
    {
    "countries":"Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    }
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["countries"] = country_visited
    new_country["total_visits"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)