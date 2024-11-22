import unittest
import numpy as np

import sys
from pathlib import Path

# Add the parent directory of the current script to sys.path
current_path = Path(__file__).resolve()
parent_directory = current_path.parent.parent  # Go up two levels to the base directory
sys.path.append(str(parent_directory))

from Fractocart.main import convert_to_fractional_coordinates, convert_to_cartesian_coordinates

#from test_arrays.dihydroazulene import unit_cell_DHA, cartesian_coordinates_DHA, fractional_coordinates_DHA
from test_arrays.anil import unit_cell_anil, cartesian_coordinates_anil, fractional_coordinates_anil


class TestCoordinateConversion(unittest.TestCase):
    """
    Unit tests for the coordinate conversion functions in the Fractocart module.
    This class tests the conversion between Cartesian and fractional coordinates,
    as well as handling of invalid inputs and edge cases.
    """

    def setUp(self):
        """
        Set up the unit cell parameters and test data for the coordinate conversion tests.
        Initializes the unit cell, Cartesian coordinates, and expected fractional coordinates.
        """

        # Example from Dihydroazulene
        self.unit_cell_anil = unit_cell_anil
        self.cartesian_coords_anil = cartesian_coordinates_anil
        self.expected_fractional_coords_anil = fractional_coordinates_anil

    def test_convert_to_fractional_coordinates(self):
        """
        Test the conversion from Cartesian coordinates to fractional coordinates.
        Asserts that the result matches the expected fractional coordinates within a tolerance.
        """

        result = convert_to_fractional_coordinates(self.cartesian_coords_anil, self.unit_cell_anil)
        np.testing.assert_almost_equal(result, self.expected_fractional_coords_anil, decimal=5)

    def test_convert_to_cartesian_coordinates(self):
        """
        Test the conversion from fractional coordinates to Cartesian coordinates.
        Asserts that the result matches the original Cartesian coordinates within a tolerance.
        """

        fractional_coords = self.expected_fractional_coords_anil
        result = convert_to_cartesian_coordinates(fractional_coords, self.unit_cell_anil)
        np.testing.assert_almost_equal(result, self.cartesian_coords_anil, decimal=5)

    def test_invalid_cartesian_input(self):
        """
        Test the conversion function with invalid Cartesian input.
        Asserts that a ValueError is raised when the input does not have the correct shape.
        """

        with self.assertRaises(ValueError):
            convert_to_fractional_coordinates(np.array([[1.0, 2.0]]), self.unit_cell_anil)

    def test_invalid_fractional_input(self):
        """
        Test the conversion function with invalid fractional input.
        Asserts that a ValueError is raised when the input does not have the correct shape.
        """

        with self.assertRaises(ValueError):
            convert_to_cartesian_coordinates(np.array([[0.2, 0.4]]), self.unit_cell_anil)

    def test_zero_param_unit_cell(self):
        """
        Test the conversion function with a zero-length unit cell.
        Asserts that a ValueError is raised when the unit cell contains a zero length.
        """

        zero_unit_cell = np.array([0.0, 5.0, 5.0, 90.0, 90.0, 90.0])
        with self.assertRaises(ValueError):
            convert_to_fractional_coordinates(self.cartesian_coords_anil, zero_unit_cell)
