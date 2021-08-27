import math as mt
import numpy as np


class Teste:
    vector = input()


class Coordinates_conversion:
    vector = np.array([1, 2, 3])

    def __init__(self, vector):
        self.vector = vector

    theta = np.arccos(vector[2] / (mt.sqrt(pow(vector[0], 2) + pow(vector[1], 2) + pow(vector[2], 2))))

    phi = np.arctan(vector[1] / (vector[0]))

    matrix_spherical_to_cartesian = np.array([[mt.sin(theta) * mt.cos(phi), mt.sin(theta) * mt.sin(phi),
                                               mt.cos(theta)],
                                              [mt.cos(theta) * mt.cos(phi), mt.cos(theta) * mt.sin(phi),
                                               -mt.sin(theta)],
                                              [-mt.sin(phi), mt.cos(phi), 0]])

    @staticmethod
    def is_vector(vector):
        if len(vector) != 3:
            return False

    def conv_cartesian_to_cylindrical(self, vector):
        cylindrical_vec = []
        if not self.is_vector(vector):
            pass

    def conv_cylindrical_to_cartesian(self, vector):
        if not self.is_vector(vector):
            pass

    def conv_cartesian_to_spherical(self, vector):
        if not self.is_vector(vector):
            pass

    def conv_spherical_to_cartesian(self, vector):
        if not self.is_vector(vector):
            pass
