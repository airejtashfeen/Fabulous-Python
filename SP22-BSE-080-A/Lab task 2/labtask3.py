from math import sin, cos, pi

def derivative_approx_sin(x, h):
    return (sin(x + h) - sin(x)) / h

def calculate_derivative(h):
    results = []
    x = -pi
    while x <= pi:
        approx_derivative = derivative_approx_sin(x, h)
        results.append((x, approx_derivative, cos(x)))
        x += 0.001
    return results

h_values = [0.001, 0.01, 0.1]

for h in h_values:
    print(f"Calculating for h = {h}")
    print(f"{'x':>10} {'Approximate d(sin(x))/dx':>30} {'cos(x)':>20}")
    for x, approx, actual in calculate_derivative(h):
        print(f"{x:>10.4f} {approx:>30.10f} {actual:>20.10f}")
    print("\n")
