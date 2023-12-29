def add_melon():
    melon = input('What melon would you like to add? ')
    price = input("How much will this melon cost? ")
    seedless = input('Is this melon seedless? ')
    flesh_color = input("What color would you say this melon's flesh is? ")
    rind_color = input("What color is it's rind? ")
    average_weight = input("How much does is weigh? ")
    melons[melon] = {'price': float(price), 'seedless': bool(seedless), 'flesh_color': flesh_color,
                     'rind_color': rind_color, 'average_weight': float(average_weight)}
    return melons

melons = {'Honeydew': {
                        'price': 0.99, 
                       'seedless': True, 
                       'flesh_color': None,
                      'rind_color': None, 
                      'average_weight': None},
          'Crenshaw': {'price': 2.00, 'seedless': False, 'flesh_color': None,
                      'rind_color': None, 'average_weight': None},
          'Crane': {'price': 2.50, 'seedless': False, 'flesh_color': None,
                      'rind_color': None, 'average_weight': None},
          'Casaba': {'price': 2.50, 'seedless': False, 'flesh_color': None,
                      'rind_color': None, 'average_weight': None},
          'Cantaloupe': {'price': .99, 'seedless': False, 'flesh_color': None,
                      'rind_color': None, 'average_weight': None},}
#add_melon()
print(melons)