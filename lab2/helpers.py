import numpy as np

rules = np.array([
    [1, 1, 6],
    [1, 2, 6],
    [1, 3, 6],
    [1, 4, 5],
    [1, 5, 5],
    [1, 6, 5],
    [2, 1, 6],
    [2, 2, 6],
    [2, 3, 6],
    [2, 4, 5],
    [2, 5, 5],
    [2, 6, 5],
    [3, 1, 6],
    [3, 2, 6],
    [3, 3, 6],
    [3, 4, 5],
    [3, 5, 5],
    [3, 6, 5],
    [4, 1, 6],
    [4, 2, 5],
    [4, 3, 4],
    [4, 4, 2],
    [4, 5, 2],
    [4, 6, 1],
    [5, 1, 5],
    [5, 2, 4],
    [5, 3, 4],
    [5, 4, 1],
    [5, 5, 1],
    [5, 6, 1],
    [6, 1, 3],
    [6, 2, 3],
    [6, 3, 3],
    [6, 4, 1],
    [6, 5, 1],
    [6, 6, 1]
])

rules2 = np.array([
    [1, 1, 6],
    [1, 2, 6],
    [1, 3, 6],
    [1, 4, 6],
    [1, 5, 6],
    [1, 6, 6],
    [2, 1, 6],
    [2, 2, 6],
    [2, 3, 6],
    [2, 4, 5],
    [2, 5, 5],
    [2, 6, 5],
    [3, 1, 6],
    [3, 2, 6],
    [3, 3, 6],
    [3, 4, 5],
    [3, 5, 5],
    [3, 6, 5],
    [4, 1, 2],
    [4, 2, 2],
    [4, 3, 2],
    [4, 4, 1],
    [4, 5, 1],
    [4, 6, 1],
    [5, 1, 2],
    [5, 2, 2],
    [5, 3, 2],
    [5, 4, 1],
    [5, 5, 1],
    [5, 6, 1],
    [6, 1, 1],
    [6, 2, 1],
    [6, 3, 1],
    [6, 4, 1],
    [6, 5, 1],
    [6, 6, 1]
])

def get_membership_function(x, a, b, c, d):
    if x <= a:
        return 0
    elif x > a and x <= b:
        return (x - a) / (b - a)
    elif x > b and x <= c:
        return 1
    elif x > c and x <= d:
        return (d - x) / (d - c)
    else:
        return 0

def get_term_membership_function(term, x):
    match term:
        case 1:
            return get_membership_function(x, -1000, -200, -100, -50)
        case 2:
            return get_membership_function(x, -100, -50, -50, -10)
        case 3:
            return get_membership_function(x, -50, -10, 0, 0)
        case 4:
            return get_membership_function(x, 0, 0, 10, 50)
        case 5:
            return get_membership_function(x, 10, 50, 50, 100)
        case 6:
            return get_membership_function(x, 50, 100, 200, 1000)

def get_general_membership_function(phi, omega, mu):
    xi_dash = 0

    for rule in rules2:
        alfa = get_term_membership_function(rule[0], phi)
        beta = get_term_membership_function(rule[1], omega)
        gama = min(alfa, beta)
        delta = get_term_membership_function(rule[2], mu)
        xi = min(gama, delta)
        if xi_dash < xi:
            xi_dash = xi

    return xi_dash