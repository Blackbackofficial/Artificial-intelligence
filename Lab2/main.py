import json
import math


def start():
    print('Введите назание первого понятия:')
    term1 = input()
    print('Введите назание второго понятия:')
    term2 = input()

    find_term = get_term(term1, term2)
    term1 = find_term[0][0]
    term2 = find_term[1][0]
    term1.pop('Law')
    term2.pop('Law')

    if term1['popular'] == 'Yes':
        term1['popular'] = 1
    else:
        term1['popular'] = 0
    if term2['popular'] == 'Yes':
        term2['popular'] = 1
    else:
        term2['popular'] = 0

    # Манхеттенское
    manx_term = manxeten(term1, term2)

    # Евклидово
    evk_term = evklidov(term1, term2)

    # Близость по дереву
    tree = proximity_tree(term1, term2)

    # Коррелляция
    cov = corraliation(term1, term2)

    print('Манхеттенское: {}'.format(manx_term))
    print('Евклидово: {}'.format(evk_term))
    print(tree)
    print('Корреляция: {}'.format(cov))


def get_term(term1, term2):
    with open('Artificial-intelligence/data.json') as data:  # Если нужно, поменяйте
        text = json.load(data)
        for element in text['node']:
            if element['Name'] == term1:
                term1 = element['Var']
            elif element['Name'] == term2:
                term2 = element['Var']
    return term1, term2


# Манхеттенское
def manxeten(term1, term2):
    term1 = sum(term1.values())
    term2 = sum(term2.values())
    manx_term = abs(term1 - term2)
    return manx_term


# Евклидово
def evklidov(term1, term2):
    term1 = list(term1.values())
    term2 = list(term2.values())
    term = [pow(term1[0] - term2[0], 2), pow(term1[1] - term2[1], 2), pow(term1[2] - term2[2], 2),
            pow(term1[3] - term2[3], 2)]
    sum_term = sum(term)
    term = math.sqrt(sum_term)
    return term


# Близость по дереву
def proximity_tree(term1, term2):
    term = term1['Level'] - term2['Level']
    if term == 0:
        return "По Дереву: 5"
    else:
        return term1['Level']


def corraliation(term1, term2):
    sr_term1 = sum(term1.values()) / 5
    sr_term2 = sum(term2.values()) / 5
    # сигма y сумма квадратичная
    list_term1 = [pow(term1["Year"] - sr_term2, 2), pow(term1["Arg"] - sr_term2, 2), pow(term1["Accuracy"] - sr_term2, 2),
                  pow(term1["Level"] - sr_term2, 2), 1]
    # сигма x сумма квадратичная
    list_term2 = [pow(term2["Year"] - sr_term1, 2), pow(term2["Arg"] - sr_term1, 2), pow(term2["Accuracy"] - sr_term1, 2),
                  pow(term2["Level"] - sr_term1, 2), 1]
    # Сигмы 1 и 2
    sigm_term1 = math.sqrt(sum(list_term1) / 5)
    sigm_term2 = math.sqrt(sum(list_term2) / 5)
    # средний term1 b term2
    term1_term2 = 1 / 5 * sum(term1.values()) * sum(term2.values())
    cov = (term1_term2 - sr_term1 * sr_term2) / (sigm_term1 * sigm_term2)
    return cov


if __name__ == '__main__':
    start()
