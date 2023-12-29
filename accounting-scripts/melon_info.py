"""Print out all the melons in our inventory."""


from melons import melons, add_melon


# def print_melon(name, price, seedless):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])

def melon_info(melons):
    #I did this because I could't figure out how to display name and then attributes in one looping scenario
    # for melon in melons:
    #     print(f"{melon}")
    #     print(f"price : {melons[melon]['price']}")
    #     print(f"seedless : {melons[melon]['seedless']}")
    #     print(f"flesh_color : {melons[melon]['flesh_color']}")
    #     print(f"rind_color : {melons[melon]['rind_color']}")
    #     print(f"average_weight : {melons[melon]['average_weight']}")
    #     print('--------------------')
    for melon_name, attributes in melons.items():
        print(melon_name)

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
        print('-----------')

print(melon_info(melons))