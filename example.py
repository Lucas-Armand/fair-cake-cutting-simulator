import cake
import pandas as pd

print("Example 1")

evaluations = pd.DataFrame({
    '2.1': [33.33, 20.00, 15.00],
    '3.1': [20.33, 30.00, 25.00],
    '4.1': [5.00, 10.00, 10.00],
    '4.2': [3.00, 5.00, 10.00],
    '4.3': [2.00, 5.00, 10.00],
    '2.3': [33.33, 30.00, 30.00]
}, index=['A', 'B', 'C'])
print()
print(evaluations)
print()
command = "A:2.1/2 => 5.1 = 4.3"  
print(command)
print()


new_evaluations, _ = cake.process_command(evaluations, command)

print(new_evaluations)
print()
print()

print("Example 2")
evaluations = pd.DataFrame({
    '2.1': [33.33, 20.00, 15.00],
    '3.1': [20.33, 30.00, 25.00],
    '4.1': [5.00, 10.00, 10.00],
    '4.2': [3.00, 5.00, 10.00],
    '4.3': [2.00, 5.00, 10.00],
    '2.3': [33.33, 30.00, 30.00]
}, index=['A', 'B', 'C'])
print()
print(evaluations)
print()

allocation_command = "A <= 2.1, 4.2; B <= 3.1, 4.1; C <= 2.3, 4.3"
print(allocation_command)
print()

final_matrix, satisfactory = cake.process_command(evaluations, allocation_command)
print(f"Satisfatória: {satisfactory}")
print(f"Matriz Final:\n{final_matrix}")
print()


