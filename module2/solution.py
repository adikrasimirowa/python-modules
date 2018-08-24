def num_add(a, b):
        return a + b

def num_sub(a, b):
        return a - b

def num_mul(a, b):
        return a * b

def num_div(a, b):
        return a / b

def num_floor(a, b):
        return a // b

def num_rem(a, b):
        return a % b

IS_TRUE = True
IS_FALSE = False

PANCAKE_INGREDIENTS = {'flour': 2, 'eggs': 4, 'milk': 200, 'butter': False, 'salt': 0.001 }

def ingredient_exists(ingr, dict):
        if ingr in dict:
            return True
        else:
            return False

def fatten_pancakes(dict):
    INGREDIENTS = dict.copy()
    INGREDIENTS['eggs'] = 6
    INGREDIENTS['butter'] = True

    return INGREDIENTS

def add_sugar(dict):
    INGREDIENTS = dict.copy()
    INGREDIENTS['sugar'] = True

    return INGREDIENTS

def remove_salt(dict):
    INGREDIENTS = dict.copy()
    del INGREDIENTS['salt'] 

    return INGREDIENTS


if __name__ == '__main__':
        print(num_add(2, 3))
        print(num_sub(3, 5))
        print(num_mul(3, 5))
        print(num_div(3, 5))
        print(num_floor(3, 5))
        print(num_rem(3, 5))
        print(ingredient_exists('coffe', PANCAKE_INGREDIENTS))
        print(fatten_pancakes(PANCAKE_INGREDIENTS))
        print(add_sugar(PANCAKE_INGREDIENTS))
        print(remove_salt(PANCAKE_INGREDIENTS))

