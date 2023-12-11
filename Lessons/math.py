Xs = [1970,1975,1980,1985,1990,1995,2000,2003,2005,2006,2008,2010,2013,2015,2017]
Ys = [0.24,0.55,1.0,1.4,1.9,2.4,3.2,3.7,4.6,5.2,6.9,8.3,9.0,9.2,9.4]

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

plt.scatter(Xs, Ys)
plt.xlabel("Year")
plt.ylabel("Population in millions")
plt.title("The population of the UAE at various times from 1970 to 2017")

coefficients = np.polyfit(Xs, np.log(Ys), deg=1)
a, b = coefficients  # Coefficients for the linear fit

a_exp = np.exp(b)
b_exp = np.exp(a)
print(a_exp, b_exp)

# Generate fitted data using the obtained coefficients
x_fit = np.linspace(min(Xs), max(Xs), 100)
y_fit = a_exp * (b_exp ** x_fit)  # Exponential fit
# Generate fitted data using the obtained coefficients
# x_fit = np.linspace(min(Xs), max(Xs), 100)
# y_fit = np.exp(a * x_fit + b)  # Exponential fit

# Plot fitted exponential curve
#plt.plot(x_fit, y_fit, 'r-', label='Fitted Exponential Curve')
equation = f'y = {a_exp} * {b_exp}^x'
print(equation)

plt.show()

y_predicted = a_exp * (b_exp ** Xs)  # Predicted values
residuals = Ys - y_predicted
ss_residual = np.sum(residuals ** 2)
ss_total = np.sum((Ys - np.mean(Ys)) ** 2)
r_squared = 1 - (ss_residual / ss_total)
print(r_squared)

# logistic regression
import math
equation = "16.313 *(1 + 75.603 *e**(-0.102x))"

plt.scatter(Xs, Ys)
plt.xlabel("Year")
plt.ylabel("Population in millions")
plt.title("The population of the UAE at various times from 1970 to 2017")

def func(x):
    return 16.313 / (1 + 75.603 * (math.e ** (-0.102 * x)))

y_fit = [func(i-1970) for i in range(1970, 2030)]
plt.plot(range(1970, 2030), y_fit, color="red")
plt.show()