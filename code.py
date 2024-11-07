from pulp import LpProblem, LpVariable, LpMinimize, lpSum

def solve_transportation_problem(costs, capacities, demands):
    # Define the number of warehouses and destinations based on the input data
    num_warehouses = len(capacities)
    num_destinations = len(demands)
    
    # Initialize the transportation problem as a minimization problem
    problem = LpProblem("Minimize_Transportation_Cost", LpMinimize)
    
    # Define decision variables for the quantity to be shipped from each warehouse to each destination
    transport_qty = LpVariable.dicts("TransportQty", 
                                     [(i, j) for i in range(num_warehouses) for j in range(num_destinations)], 
                                     lowBound=0)
    
    # Objective function: Minimize the total transportation cost
    problem += lpSum(costs[i][j] * transport_qty[(i, j)] 
                     for i in range(num_warehouses) 
                     for j in range(num_destinations)), "Total_Transportation_Cost"
    
    # Supply constraints: Total shipments from each warehouse should not exceed its capacity
    for i in range(num_warehouses):
        problem += lpSum(transport_qty[(i, j)] for j in range(num_destinations)) <= capacities[i], \
                   f"Warehouse_{i+1}_Capacity"
    
    # Demand constraints: Total shipments to each destination should meet its demand
    for j in range(num_destinations):
        problem += lpSum(transport_qty[(i, j)] for i in range(num_warehouses)) >= demands[j], \
                   f"Destination_{j+1}_Demand"
    
    # Solve the problem
    problem.solve()
    
    # Retrieve results
    total_cost = problem.objective.value()
    solution = {(i+1, j+1): transport_qty[(i, j)].value() for i in range(num_warehouses) for j in range(num_destinations)}

    return total_cost, solution

# Define input data
costs = [
    [15, 160, 154, 245, 130, 125, 215],
    [160, 12, 315, 410, 290, 427, 375],
    [100, 260, 56, 190, 58, 204, 160]
]
capacities = [3980, 1785, 4856]
demands = [1168, 1560, 1439, 986, 1658, 2035, 1159]

# Solve the problem
total_cost, solution = solve_transportation_problem(costs, capacities, demands)

# Print the results
print(f"Total Transportation Cost: {total_cost:.2f}")
for (i, j), qty in solution.items():
    print(f"Optimal Transport Qty from Warehouse {i} to Destination {j}: {qty:.2f}")
