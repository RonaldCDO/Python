import numpy as np
import math as mt

__author__ = 'Ronald'
__email__ = 'ronaldcesar.eng@gmail.com'

# Values of the equation
# q1 = 1 * pow(10, -9)
# q2 = -10 * pow(10, -9)
# r_1 = np.array([10, -8, -3])
# r_2 = np.array([-3, 5, 4])
# r_3 = np.array([9, 5, 8])
# E_0 = 8.854 * pow(10, -12)
# K_1 = q1 / (4 * mt.pi * E_0 * mt.sqrt(pow(pow((r_3[0] - r_1[0]), 2) + pow((r_3[1] - r_1[1]), 2) +
#                                           pow((r_3[2] - r_1[2]), 2), 3)))
# K_2 = q2 / (4 * mt.pi * E_0 * mt.sqrt(pow(pow((r_3[0] - r_2[0]), 2) + pow((r_3[1] - r_2[1]), 2) +
#                                           pow((r_3[2] - r_2[2]), 2), 3)))
# vector_dif1 = r_3 - r_1
# vector_dif2 = r_3 - r_2
#
# theta = np.arccos(r_3[2] / (mt.sqrt(pow(r_3[0], 2) + pow(r_3[1], 2) +
#                                     pow(r_3[2], 2))))
# phi = np.arctan(r_3[1] / (r_3[0]))
#
# m1 = np.array([[mt.sin(theta) * mt.cos(phi), mt.sin(theta) * mt.sin(phi),
#                 mt.cos(theta)],
#                [mt.cos(theta) * mt.cos(phi), mt.cos(theta) * mt.sin(phi),
#                 -mt.sin(theta)],
#                [-mt.sin(phi), mt.cos(phi), 0]])
#
# E_vec = K_1 * vector_dif1 + K_2 * vector_dif2
#
# E_spherical_coordinates = np.array([m1[0][0] * E_vec[0] + m1[0][1] * E_vec[1] + m1[0][2] * E_vec[2],
#                                     m1[1][0] * E_vec[0] + m1[1][1] * E_vec[1] + m1[1][2] * E_vec[2],
#                                     m1[2][0] * E_vec[0] + m1[2][1] * E_vec[1] + m1[2][2] * E_vec[2]])
# dict_visualization = {'E_r': E_spherical_coordinates[0], 'E_theta': E_spherical_coordinates[1],
#                       'E_phi': E_spherical_coordinates[2]}
# print(dict_visualization)


class Electric_Charge:
    PI = mt.pi
    E_1 = 8.854 * pow(10, -12)
    K = 1 / (4 * PI * E_1)
    vec_dif = []

    def __init__(self, charge, charge_coordinates):
        self.charge = charge
        self.charge_coordinates = charge_coordinates

    def electric_field_calc(self, actual_coordinates):
        self.vec_dif = actual_coordinates - self.charge_coordinates
        return self.K * self.charge * self.vec_dif

    # def coordinates_conversion(self, E_vec , coordinates_type):
    #     if coordinates_type == 's':
    #         m1 = np.array([[mt.sin(theta) * mt.cos(phi), mt.sin(theta) * mt.sin(phi),
    #                         mt.cos(theta)],
    #                        [mt.cos(theta) * mt.cos(phi), mt.cos(theta) * mt.sin(phi),
    #                         -mt.sin(theta)],
    #                        [-mt.sin(phi), mt.cos(phi), 0]])
    #
    #         E_spherical_coordinates = np.array([m1[0][0] * E_vec[0] + m1[0][1] * E_vec[1] + m1[0][2] * E_vec[2],
    #                                 m1[1][0] * E_vec[0] + m1[1][1] * E_vec[1] + m1[1][2] * E_vec[2],
    #                                 m1[2][0] * E_vec[0] + m1[2][1] * E_vec[1] + m1[2][2] * E_vec[2]])


e1 = Electric_Charge(1 * pow(10, -9), np.array([1, 2, 3]))
print(e1.electric_field_calc(np.array([3, 2, 1])))

# print(np.array([2, 0, -2]) * 1 * pow(10, -9) * e1.K / pow(mt.sqrt(8), 3))
