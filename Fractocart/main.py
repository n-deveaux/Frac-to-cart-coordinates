import numpy as np

def _build_transformation_matrix(unit_cell: np.ndarray) -> np.ndarray:
    """
    Construct the transformation matrix to fractionalize the coordinates.
    
    :param unit_cell: an array containing the unit cell parameters in the order: a, b, c, alpha, beta, gamma.
    :return: a 3x3 transformation matrix.
    """

    if not isinstance(unit_cell, np.ndarray) or unit_cell.shape != (6,):
        raise ValueError("unit_cell must be a numpy array of shape (6,)")

    # Define unit cell parameters with angles in radians
    a = unit_cell[0]
    b = unit_cell[1]
    c = unit_cell[2]
    alpha = np.deg2rad(unit_cell[3])
    beta = np.deg2rad(unit_cell[4])
    gamma = np.deg2rad(unit_cell[5])

    cos_alpha_star = ((np.cos(beta)) * np.cos(gamma) - np.cos(alpha)) / (np.sin(beta) * np.sin(gamma))
    sin_alpha_star = np.sqrt(1 - cos_alpha_star**2)

    transformation_matrix = np.array([
        [a, b * np.cos(gamma), c * np.cos(beta)],
        [0, b * np.sin(gamma), -c * np.sin(beta) * cos_alpha_star],
        [0, 0, c * np.sin(beta) * sin_alpha_star]
    ])

    return transformation_matrix

def convert_to_fractional_coordinates(coord_atoms: np.ndarray, unit_cell: np.ndarray) -> np.ndarray:
    """
    Convert an array of atomic coordinates to fractional coordinates.

    :param coord_atoms: An array with lists of xyz coordinates in angstrom of the atoms as elements.
    :param unit_cell: An array containing the unit cell parameters in the order: a, b, c, alpha, beta, gamma.

    :return: An array with lists of fractional coordinates of the atoms as elements.
    """

    if not isinstance(coord_atoms, np.ndarray) or coord_atoms.ndim != 2 or coord_atoms.shape[1] != 3:
        raise ValueError("coord_atoms must be a numpy array of shape (n, 3) where n is the number of atoms.")

    transformation_matrix = _build_transformation_matrix(unit_cell)
    fractional_coordinates = np.dot(coord_atoms, np.linalg.inv(transformation_matrix))

    return fractional_coordinates