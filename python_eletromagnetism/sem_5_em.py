import math as mt

# Question 1
I = 10
sigma_1 = 1508.5
sigma_2 = 3630
a = 0.001
c = 0.007
b = 0.010
d = 0.07
l = 0.02
tg_alpha = (c-a)/l
tg_beta = (d-b)/l
x0 = a/tg_alpha
X0 = b/tg_beta

R1 = (1/(sigma_1*mt.pi*pow(tg_alpha,2)))*(-1/(l+x0) - (-1/x0))
R2 = (1/(sigma_2*mt.pi*pow(tg_beta,2)))*(-1/(l+X0) - (-1/X0))
 
req = (R1 * R2)/(R1+R2)
V = req*I
print(f"DDP: {V} V")


# Question 2
a_2 = 1*pow(10,-3)
b_2 = 8*pow(10,-3)
eps_2 = 8.854*pow(10,-12)
t_1 = 4
t_2 = 13
cap = eps_2*4*mt.pi*(t_1+t_2)/(pow(b_2,4) - pow(a,4))
print(f"Capacity: {cap} F/m")