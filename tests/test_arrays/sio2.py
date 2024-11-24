import numpy as np

"""
Example of an SiO_2 crystal from the space group 182.
"""

# Define unit cell parameters: [a, b, c, alpha, beta, gamma]
unit_cell_sio2 = np.array([5.12731424, 5.12731424, 8.70045567, 90.00, 90.00, 120.00])

cartesian_coordinates_sio2 = np.array([
    [2.5636570454, 1.4801281691, 6.5253419876],
    [2.5636571200, 1.4801281283, 8.1522245045],
    [4.0649199163, 1.8401209464, 8.7004556700]
])

fractional_coordinates_sio2 = np.array([
    [0.6666666667, 0.3333333333, 0.7500000000],
    [0.6666666667, 0.3333333333, 0.9369882238],
    [1.0000000000, 0.4144057782, 1.0000000000]
])