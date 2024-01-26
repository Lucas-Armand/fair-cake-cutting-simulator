import numpy as np
import pandas as pd
import random
import math


def random_choice(lst, rand_key):
    return lst[int(rand_key * len(lst))]


def random_sample(lst, k, rand_key, jump=2654435761):  # jump é um número primo grande
    sample = []
    current_key = rand_key
    for _ in range(k):
        item = random_choice(lst, current_key)
    while item in sample:  # Garantir unicidade
        current_key = (current_key * jump) % 1.0
        item = random_choice(lst, current_key)
        sample.append(item)
        current_key = (current_key * jump) % 1.0
    return sample


def random_int(a, b, rand_key):
    return a + int(rand_key * (b - a + 1))


def k_esima_permutacao(lista, k):
    """ Retorna a k-ésima permutação de uma lista. """
    n = len(lista)
    permutacao = []
    numeros = list(lista)
    k -= 1  # Ajusta para base 0

    for i in range(n, 0, -1):
        # Determina qual número deve estar na posição atual
        posicao_atual, k = divmod(k, math.factorial(i - 1))
        permutacao.append(numeros.pop(posicao_atual))

    return permutacao


def generate_random_command(evaluations, max_splits=3, rand_key=None):
    agents = evaluations.index.tolist()
    pieces = evaluations.columns.tolist()

    rand_0 = random.random()
    rand_1 = random.random()
    rand_2 = random.random()
    rand_3 = random.random()
    rand_4 = random.random()
    rand_5 = random.random()
    rand_6 = random.random()
    rand_7 = random.random()
    rand_8 = random.random()
    rand_9 = random.random()

    if rand_0 < 0.2:
        # Comando de avaliação
        allocation = {}
        for agent in agents:
            num_pieces = random_int(1, len(pieces), rand_1)
            allocated_pieces = random_sample(pieces, num_pieces, rand_2)
            allocation[agent] = allocated_pieces

        allocation_command = "; ".join([f"{agent} <= {', '.join(allocation[agent])}" for agent in allocation])
        return allocation_command
    else:
        # Comando de atualização
        agent = random_choice(agents, rand_3)
        piece = random_choice(pieces, rand_4)
        num_splits = random_int(2, len(agents), rand_5)

        # Encontrar o maior número de interação nas colunas existentes
        max_interaction_num = max(int(col.split('.')[0]) for col in evaluations.columns if '.' in col)
        new_interaction_num = max_interaction_num + 1

        if rand_6 < 0.7:
            # Todos os subpedaços iguais
            update_command = f"{agent}:{piece}/{num_splits} => " + " = ".join([f'{new_interaction_num}.{i+1}' for i in range(num_splits)])
        else:
            # Condições de igualdade aleatórias
            equal_pieces = random_sample([f"{new_interaction_num}.{i+1}" for i in range(num_splits)], random_int(1, num_splits - 1, rand_7), rand_8)
            target_piece = random_choice(pieces, rand_9)
            equal_conditions = " = ".join(equal_pieces)
            update_command = f"{agent}:{piece}/{num_splits} => {equal_conditions} = {target_piece}"

        return update_command


if __name__ == '__main__':

    evaluations = pd.DataFrame({
        '2.1': [33.33, 20.00, 15.00],
        '3.1': [20.33, 30.00, 25.00],
        '4.1': [5.00, 10.00, 10.00],
        '4.2': [3.00, 5.00, 10.00],
        '4.3': [2.00, 5.00, 10.00],
        '2.3': [33.33, 30.00, 30.00]
    }, index=['A', 'B', 'C'])

    for i in range(10):
        print(generate_random_command(evaluations, max_splits=3))

