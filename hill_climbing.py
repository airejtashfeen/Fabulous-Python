import random

def objective_function(x):
    # Example function: f(x) = -1 * (x - 3) ** 2 + 9
    return -1 * (x - 3) ** 2 + 9

def hill_climbing(starting_point, step_size, max_iterations):
    current_point = starting_point
    current_value = objective_function(current_point)

    for _ in range(max_iterations):
        # Generate new points around the current point
        neighbors = [current_point + step_size, current_point - step_size]
        
        # Find the neighbor with the highest value
        next_point = max(neighbors, key=objective_function)
        next_value = objective_function(next_point)

        # If the next point is better, move to it
        if next_value > current_value:
            current_point = next_point
            current_value = next_value
        else:
            break  # No better neighbors, exit the loop

    return current_point, current_value

# Example usage
starting_point = random.uniform(0, 6)  # Start at a random point between 0 and 6
step_size = 0.1  # Step size
max_iterations = 100  # Max iterations

optimal_point, optimal_value = hill_climbing(starting_point, step_size, max_iterations)
print(f"Optimal Point: {optimal_point}, Optimal Value: {optimal_value}")