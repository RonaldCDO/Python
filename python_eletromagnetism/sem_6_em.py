import math as mt

rho = 0.010
a = 0.002
b = 0.005
t1 = 41

H = -t1*(rho)/3*a
H_2 = (t1*(2*pow(b,3) - pow(a,3) - pow(rho,3)))/(3*a*rho)

print(f"H = {H_2} A/m")