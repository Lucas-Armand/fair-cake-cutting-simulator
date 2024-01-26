import numpy as np
import pandas as pd

def process_command(evaluations, command):
    if ':' in command:
        return update_evaluations(evaluations, command)
    elif '<=' in command:
        return is_allocation_satisfactory(evaluations, command)
    else:
        raise ValueError("Unrecognized command")
        return None, False

def update_evaluations(evaluations, command, alpha=5):
    # Extract information from the command
    participant, division = command.split(':')
    division_details, equal_division = division.split('=>')
    part, num_splits = division_details.split('/')
    num_splits = int(num_splits)
    equal_parts = equal_division.split('=')

    # Find the highest interaction number in existing columns
    max_interaction_num = max(int(col.split('.')[0]) for col in evaluations.columns if '.' in col)
    new_interaction_num = max_interaction_num + 1

    # Create names for new columns
    new_parts = [f"{new_interaction_num}.{i+1}" for i in range(num_splits)]
    
    # Find the position of the column to be replaced
    part_to_divide = part.strip()
    column_index = list(evaluations.columns).index(part_to_divide)

    # Prepare DataFrame for new columns
    for new_part in new_parts[::-1]:
        evaluations.insert(column_index, new_part, 0.0)

    # Divide the selected part
    if part_to_divide in evaluations.columns:
        for row in evaluations.index:
            if row == participant:
                # Equal division for the participant performing the action
                equal_value = evaluations.at[row, part_to_divide] / float(num_splits)
                equal_value = equal_value  # Ensure it's a float value
                for new_part in new_parts:
                    evaluations.at[row, new_part] = equal_value
            else:
                # Random division for other participants
                original_value = evaluations.at[row, part_to_divide]
                split_values = np.random.dirichlet(np.ones(num_splits) * alpha, 1)[0] * original_value
                split_values = [float(val) for val in split_values]  # Ensure these are float values
                for new_part, split_value in zip(new_parts, split_values):
                    evaluations.at[row, new_part] = split_value

        # Remove the old column
        evaluations.drop(columns=[part_to_divide], inplace=True)
    else:
        raise ValueError("Specified part is not valid or does not exist")
        return None, False

    return evaluations.round(5), None

def is_allocation_satisfactory(evaluations, allocation_command):
    # Interpret the allocation command
    allocations = allocation_command.split(';')
    allocated_parts = {part.strip().split(' <= ')[0]: part.strip().split(' <= ')[1].split(', ') for part in allocations}
    
    # Create a matrix to store each participant's evaluations for each part
    final_matrix = pd.DataFrame(0, index=evaluations.index, columns=evaluations.index)

    # Fill the matrix with corresponding evaluations
    for agent in allocated_parts.keys():
        for part in allocated_parts[agent]:
            final_matrix[agent] += evaluations[part]
    
    # Check if the allocation is satisfactory
    satisfactory = all(final_matrix.loc[agent, agent] == final_matrix.loc[agent].max() for agent in final_matrix.index)

    # Return if it's satisfactory and the final matrix
    return final_matrix, satisfactory

if __name__=="__main__":
    evaluations = pd.DataFrame({
        '1.1': [100, 100, 100]
    }, index=['A', 'B', 'C'])
    print("Initial situation:\n", evaluations)

    command = "A:1.1/3 => 2.1 = 2.2 = 2.3"
    evaluations,_ = process_command(evaluations, command)
    print('')
    print(command)
    print('')
    print("\nAfter A's command:\n", evaluations)

    command = "B:2.2/2 => 3.1 = 2.3"
    evaluations,_ = process_command(evaluations, command)
    print('')
    print(command)
    print('')
    print("\nAfter B's command:\n", evaluations)

    command = "C:3.2/3 => 4.1 = 4.2 = 4.3"
    evaluations,_ = process_command(evaluations, command)
    print('')
    print(command)
    print('')
    print("\nAfter C's command:\n", evaluations)

    allocation_command = "A <= 2.1, 4.2; B <= 3.1, 4.1; C <= 2.3, 4.3"
    print('')
    print(allocation_command)
    print('')
    final_matrix, satisfactory = process_command(evaluations, allocation_command)
    print("\nIs the allocation satisfactory:", satisfactory)
    print("\nFinal Matrix:\n", final_matrix)
