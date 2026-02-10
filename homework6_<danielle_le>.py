# web_users = ["Danielle","Clancy","Paulie","Dexter","Frankie"]
# print(web_users)

# new_users = ["Danielle","Clancy","Charles","Otis","Murphy"]
# print(new_users)

# for user in new_users:
#     if user in web_users:
#         print("This user name is already in use. Please choose different username")
#     else: 
#         print("This user name is available.")

# for user in new_users:
#     if user in web_users:
#         print("Please choose a different user name.")
#     else:
#         print("This user name is available.")

cities = {
    "New York":{
        "country":"United States",
        "population": 8400000,
        "fact":"It is home to Central Park."
    },
    "Trinidad": {
        "country":"Trinidad and Tobago",
        "population":1300000,
        "fact": "It is know for its Carnival festival."
    },
    "Ho Chi Minh": {
        "country":"Vietnam",
        "population": 9000000,
        "fact": "It is the largest city in Vietnam."
    },
}

for city, info in cities.items():
    print(f"City: {city}, Country: {info['country']}, Population: {info['population']}, Fact: {info['fact']}")