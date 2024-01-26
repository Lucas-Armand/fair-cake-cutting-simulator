# Fair Cake-Cutting Simulator

## Project Description
The Fair Cake-Cutting Simulator is a computational tool for exploring the fair division problem in game theory and economics. It simulates various strategies for dividing a resource (symbolized as a cake) among participants to achieve fairness and envy-free outcomes.

## Features
Dynamic Command Processing: The simulator includes functions for processing commands related to cake division and evaluating allocation satisfaction.
Envy-Free Division: It aims to divide a cake in a way that is perceived as fair by all participants.
Simulation of Different Scenarios: Users can simulate various scenarios with different perceptions of value among participants.

## How to Use
* Setup: Clone the repository and install the required libraries (numpy, pandas).
* Running Simulations: Use cake.py for the core functionalities. It includes functions to process division commands and check allocation satisfaction.
* Examples: example.py provides examples of how to use the simulator to divide a cake among participants and evaluate the fairness of the allocation.

## Example Usage

```python
# Sample code snippet from example.py
import cake
import pandas as pd

# Example of initializing evaluations and processing commands
# Start with one holly cake:
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
```

## Contributions

Contributions are welcome. Please read the contribution guidelines before submitting a pull request.

## License

[Specify the License if applicable]
