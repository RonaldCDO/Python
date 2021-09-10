import math as mt

# Question 1
a = 183
b = 61

q = -2.9
t1 = 2
t2 = 8
q1 = 19 * mt.pi / 180
q2 = 68 * mt.pi / 180

w_ab = q * ((a * mt.cos(q1) / 3) * (1 / pow(t2, 3) - 1 / pow(t1, 3)) + b / pow(t2, 4) * (mt.cos(q2) - mt.cos(q1)))
print("W_ab:", w_ab)

# Question 2
c = 10
eps = 8.854 * pow(10, -12)
alpha1 = 2.4
alpha2 = 8.6
beta1 = 0
beta2 = 2 * mt.pi
gamma1 = 0
gamma2 = 7.1

q = -c * (-1 / alpha2 + 1 / alpha1) * (beta2 - beta1) * (gamma2 - gamma1)

print("Error:", c)
print("Value that i got:", q)
print("Abs:", mt.sqrt(pow(q, 2)))
