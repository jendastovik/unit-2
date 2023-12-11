import numpy as np
import matplotlib.pyplot as plt

year = [1970,1975,1980,1985,1990,1995,2000,2003,2005,2006,2008,2010]
x = [i - 1970 for i in year]
# Sample scattered data (replace with your data)
x_data = np.array(x)
y_data = np.array([0.24,0.55,1.0,1.4,1.9,2.4,3.2,3.7,4.6,5.2,6.9,8.3])

# Scatter plot of the data points
plt.scatter(x_data, y_data, label='Scattered Data')

# Transform data for fitting an exponential function
log_y_data = np.log(y_data)  # Take the natural logarithm of y_data

# Fit the transformed data with a linear function using polyfit
coefficients = np.polyfit(x_data, log_y_data, deg=1)
a, b = coefficients  # Coefficients for the linear fit

# Calculate 'a' and 'b' for the exponential equation y = a * b^x
a_exp = np.exp(b)
b_exp = np.exp(a)

# Generate fitted data using the obtained coefficients
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = a_exp * (b_exp ** x_fit)  # Exponential fit

# Calculate R-squared value
y_predicted = a_exp * (b_exp ** x_data)  # Predicted values
residuals = y_data - y_predicted
ss_residual = np.sum(residuals ** 2)
ss_total = np.sum((y_data - np.mean(y_data)) ** 2)
r_squared = 1 - (ss_residual / ss_total)

# Plot fitted exponential curve
plt.plot(x_fit, y_fit, 'r-', label='Fitted Exponential Curve')

# Print the equation of the fitted exponential function and R-squared value
equation = f'y = {a_exp:.4f} * {b_exp:.4f}^x'
plt.text(2, 50, equation, fontsize=10, color='black')
print(equation)

r_squared_text = f'R-squared: {r_squared:.4f}'
plt.text(2, 40, r_squared_text, fontsize=10, color='black')
print(r_squared_text)

# Set plot labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()
