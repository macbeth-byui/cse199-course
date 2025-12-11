# CSE 199 - Training B

def convert_cups(cups):
    '''
    Convert cups to tablespoons and teaspoons
    '''
    return (cups, 16*cups, 48*cups)

def convert_tbsp(tbsp):
    '''
    Convert tablespoons to cups and teaspoons
    '''
    return (tbsp/16, tbsp, 3*tbsp)

def convert_tsp(tsp):
    '''
    Convert teaspoons to cups and tablespoons
    '''
    return (tsp/48, tsp/3, tsp)