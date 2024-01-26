import numpy as np
import pandas as pd

def process_command(evaluations, command):
    if ':' in command:
        return update_evaluations(evaluations, command)
    elif '<=' in command:
        return is_allocation_satisfactory(evaluations, command)
    else:
        raise ValueError("Comando não reconhecido")
        return None, False


def update_evaluations(evaluations, command, alpha=5):
    # Extrair informações do comando
    participant, division = command.split(':')
    division_details, equal_division = division.split('=>')
    part, num_splits = division_details.split('/')
    num_splits = int(num_splits)
    equal_parts = equal_division.split('=')

    # Encontrar o maior número de interação nas colunas existentes
    max_interaction_num = max(int(col.split('.')[0]) for col in evaluations.columns if '.' in col)
    new_interaction_num = max_interaction_num + 1

    # Criar nomes para as novas colunas
    new_parts = [f"{new_interaction_num}.{i+1}" for i in range(num_splits)]
    
    # Encontrar a posição da coluna a ser substituída
    part_to_divide = part.strip()
    column_index = list(evaluations.columns).index(part_to_divide)

    # Preparar DataFrame para novas colunas
    for new_part in new_parts[::-1]:
        evaluations.insert(column_index, new_part, 0.0)

    # Dividir a parte selecionada
    if part_to_divide in evaluations.columns:
        for row in evaluations.index:
           if row == participant:
               # Divisão igual para o participante que executa a ação
               equal_value = evaluations.at[row, part_to_divide] / float(num_splits)
               equal_value = equal_value  # Garantir que é um valor de ponto flutuante
               for new_part in new_parts:
                   evaluations.at[row, new_part] = equal_value
           else:
               # Divisão aleatória para os outros participantes
               original_value = evaluations.at[row, part_to_divide]
               split_values = np.random.dirichlet(np.ones(num_splits) * alpha, 1)[0] * original_value
               split_values = [float(val) for val in split_values]  # Garantir que são valores de ponto flutuante
               for new_part, split_value in zip(new_parts, split_values):
                   evaluations.at[row, new_part] = split_value

        # Remover a coluna antiga
        evaluations.drop(columns=[part_to_divide], inplace=True)
    else:
        raise ValueError("Parte especificada não é válida ou não existe")
        return None, False

    return evaluations.round(5), None
    
    
def is_allocation_satisfactory(evaluations, allocation_command):
    # Interpretar o comando de alocação
    allocations = allocation_command.split(';')
    allocated_parts = {part.strip().split(' <= ')[0]: part.strip().split(' <= ')[1].split(', ') for part in allocations}
    
    # Criar uma matriz para armazenar as avaliações de cada participante para cada parte
    final_matrix = pd.DataFrame(0, index=evaluations.index, columns=evaluations.index)

    # Preencher a matriz com as avaliações correspondentes
    for agent in allocated_parts.keys():
        for part in allocated_parts[agent]:
            final_matrix[agent] += evaluations[part]
    
    # Verificar se a alocação é satisfatória
    satisfactory = all(final_matrix.loc[agent, agent] == final_matrix.loc[agent].max() for agent in final_matrix.index)

    # Retornar se é satisfatória e a matriz final
    return final_matrix, satisfactory


if __name__=="__main__":

	evaluations = pd.DataFrame({
	    '1.1': [100, 100, 100]
	}, index=['A', 'B', 'C'])
	print("Situação inicial:\n", evaluations)


	command = "A:1.1/3 => 2.1 = 2.2 = 2.3"
	evaluations,_ = process_command(evaluations, command)
	print('')
	print(command)
	print('')
	print("\nApós o comando de A:\n", evaluations)


	command = "B:2.2/2 => 3.1 = 2.3"
	evaluations,_ = process_command(evaluations, command)
	print('')
	print(command)
	print('')
	print("\nApós o comando de B:\n", evaluations)

	command = "C:3.2/3 => 4.1 = 4.2 = 4.3"
	evaluations,_ = process_command(evaluations, command)
	print('')
	print(command)
	print('')
	print("\nApós o comando de C:\n", evaluations)


	allocation_command = "A <= 2.1, 4.2; B <= 3.1, 4.1; C <= 2.3, 4.3"
	print('')
	print(allocation_command)
	print('')
	final_matrix, satisfactory = process_command(evaluations, allocation_command)
	print("\nAlocação é satisfatória:", satisfactory)
	print("\nMatriz Final:\n", final_matrix)

