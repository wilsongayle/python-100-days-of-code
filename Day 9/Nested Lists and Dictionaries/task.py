travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print D
print(nested_list[2][1])

travel_log_dictionary = {
    "France": {
        "total_visits": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "total_visits": 8,
        "cities_visited": ["Stuttgart", "Berlin"],
    }
}

# print Stuttgart
print(travel_log_dictionary["Germany"]["cities_visited"][0])