def convert_cups(cups):
    return (cups, 16*cups, 48*cups)

def convert_tbsp(tbsp):
    return (tbsp/16, tbsp, 3*tbsp)

def convert_tsp(tsp):
    return (tsp/48, tsp/3, tsp)