import math as mt

micro_0 = 4*mt.pi*pow(10,-7)
t1 = 42
micro = 1*pow(10,-6)
rho_0 = 4.9
phi = 12*mt.pi/180
l = 2.9

electric_flow2 = 3*micro/micro_0 * mt.tan(phi)*l*rho_0
print(f"I = {electric_flow2} A") 

a = 0.03
b = 0.06
c = 0.15

magnetic_flow_2 = (micro_0*t1/(3*a))*(pow(a,3) - pow(c,3) + pow(b,3))*((pow(b,4) - pow(a,4))/4)
print(f"Io_m = {magnetic_flow_2} Wb/m^2")