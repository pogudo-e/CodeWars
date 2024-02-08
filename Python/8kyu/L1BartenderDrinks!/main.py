def get_drink_by_profession(param):
    dict = {"Jabroni": "Patron Tequila",
            "School Counselor": "Anything with Alcohol",
            "Programmer": "Hipster Craft Beer",
            "Bike Gang Member": "Moonshine",
            "Politician": "Your tax dollars",
            "Rapper": "Cristal"}
    return dict[param.title()] if param.title() in dict.keys() else "Beer"


print(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")