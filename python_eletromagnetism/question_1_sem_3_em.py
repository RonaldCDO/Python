import math as mt

# values of the question
r = 2.3 * pow(10, -2)
a = pow(10, -2)
b = 4 * pow(10, -2)
v = 8 * pow(10, -3)
rho_esf = v * pow(r, 2)
theta = 53 * mt.pi / 180
phi = 48 * mt.pi / 180
eps = 8.854 * pow(10, -12)

# electrical field
E_r = v * (pow(r, 5) - pow(a, 5)) / (5 * eps * pow(r, 2))
print(E_r)
