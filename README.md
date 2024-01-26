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
import numpy as np
import pandas as pd
import cake

# Initial Values: 
# Each participant (A, B, and C) assigns a total value of 100 to the cake. 
# This suggests that each participant views the cake as having the same total value.
evaluations = pd.DataFrame({'1.1': [100, 100, 100]}, index=['A', 'B', 'C'])
# Display initial situation
print("Initial situation:\n", evaluations)

# First Round - "A" decides:
# A:(1.1/3 => 2.1 = 2.2 = 2.3): A divides the cake (1.1) into three equal parts (in their opinion).
# Each part is valued by A as having one-third of the total value of the cake (33.33 each).
command = "A:1.1/3 => 2.1 = 2.2 = 2.3"
evaluations, _ = cake.process_command(evaluations, command)
# Display evaluations after A's command
print("\nAfter A's command:\n", evaluations)

# Second Round - "B" decides:
# B:(2.2/2 => 3.1 = 2.3): B divides part (2.2) into two parts (3.1 and 3.2), 
# such that (3.1) has the same value as (2.3) (in their opinion). Part (2.3) remains intact.
command = "B:2.2/2 => 3.1 = 2.3"
evaluations, _ = cake.process_command(evaluations, command)
# Display evaluations after B's command
print("\nAfter B's command:\n", evaluations)

# Third Round - "C" decides:
# C:(3.2/3 => 4.1 = 4.2 = 4.3): C divides part (3.2) into three equal parts.
# Parts (2.1), (3.1), and (2.3) remain as they are.
command = "C:3.2/3 => 4.1 = 4.2 = 4.3"
evaluations, _ = cake.process_command(evaluations, command)
# Display evaluations after C's command
print("\nAfter C's command:\n", evaluations)

# Final Decision:
# The final choice of each participant is given, for example, A <= 2.1, indicating A chooses part (2.1).
# Final values for each participant are summed up, showing how each evaluated their final part.
allocation_command = "A <= 2.1, 4.2; B <= 3.1, 4.1; C <= 2.3, 4.3"
final_matrix, satisfactory = cake.process_command(evaluations, allocation_command)
# Display if the allocation is satisfactory and the final matrix
print("\nIs the allocation satisfactory:", satisfactory)
print("\nFinal Matrix:\n", final_matrix)
```

## Contributions

Contributions are welcome. Please read the contribution guidelines before submitting a pull request.

## License

[Specify the License if applicable]
