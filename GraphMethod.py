import numpy as np
import matplotlib.pyplot as plt

# 2
# 2 0 <= 12
# -2 2 >= 6
#
# 0 -3 54


num = int(input("Enter the number of constraints: "))

print("Enter constraints: ")
constraints = list()
for i in range(0, num):
    constraints += input()

objFun = input("Enter objective function coefficients: ")



# Create a grid and a mesh of x values
x1 = np.linspace(0, 20, 400)
x2 = np.linspace(0, 20, 400)

X1, X2 = np.meshgrid(x1, x2)

# Constraint equations
# 2x1 <= 12 -> x1 <= 6
constraint1 = X1 <= 6

# -2x1 + 2x2 >= 6 -> x2 >= 3 + x1
constraint2 = X2 >= 3 + X1

# Combine constraints
feasible_region = constraint1 & constraint2

# Objective Function
F = -3 * X2 + 54

# Create a plot
plt.figure(figsize=(10, 8))

# Add x, y axis
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)


# Highlight the feasible region
plt.imshow(feasible_region, extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3)

# Plot constraint lines
plt.plot(x1, 3 + x1, 'r-', linewidth=2, label=r'$-2x_1 + 2x_2 \geq 6$')
plt.axvline(6, color='b', linewidth=2, label=r'$2x_1 \leq 12$')
# Set limits for better visualization
plt.xlim((-10, 20))
plt.ylim((-10, 20))


# Add labels and legend
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Optimization Problem')
plt.legend()

# Mark the corner points
corners = [(0, 3)]
for corner in corners:
    plt.plot(*corner, 'ro')
    plt.text(corner[0], corner[1], f'({corner[0]}, {corner[1]})', verticalalignment='bottom')

# Calculate the function value at corner points
for x1, x2 in corners:
    plt.annotate(f"F={-3*x2 + 54}", (x1, x2), textcoords="offset points", xytext=(-10,10), ha='center')

print(f"\nThe maximum value of F={-3*x2 + 54} at point (0, 3)")
plt.show()